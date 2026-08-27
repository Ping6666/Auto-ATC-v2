from typing import Dict, List, Callable

from tqdm import tqdm
from torch.utils.data import DataLoader
from torch.nn.parallel import DistributedDataParallel as DDP
import numpy as np
import torch

from core.utils import get_noise_like
from core.diffuser import DDPM, DDIM, FlowMatching
from core.model.module import TrajGen
from core.pipeline.utils import torch_mse, torch_error


class Pipeline():

    def __init__(
        self,
        batch_to: Callable,
        model: torch.nn.Module,
        optimizer_kwargs: Dict,
    ):
        self.batch_to = batch_to
        self.model = model

        self.model_handler = None
        if isinstance(self.model, DDP):
            self.model_handler = self.model.module
        else:
            self.model_handler = self.model

        #

        self.model_params = list(self.model.parameters())
        if not self.model_params:
            raise ValueError
        self.device = self.model_params[0].device

        # _opt_algo = torch.optim.SGD
        _opt_algo = torch.optim.AdamW
        self.optimizer = _opt_algo(self.model_params, **optimizer_kwargs)
        return

    def _set_train(self):
        self.model.train()
        return

    def _set_eval(self):
        self.model.eval()
        return

    def _train(self):
        raise NotImplementedError

    def _inference(self):
        raise NotImplementedError

    def train(
        self,
        train_dl: DataLoader,
        val_dl: DataLoader = None,
        use_pbar: bool = True,
    ):
        batch: torch.Tensor
        _losses: torch.Tensor
        _val_losses: torch.Tensor

        self._set_train()

        num_loss_item = None
        losses = []
        val_losses = []

        # --- train --- #

        pbar = tqdm(train_dl, leave=False) if use_pbar else train_dl

        for batch in pbar:
            bs, _batch = self.batch_to(batch, self.device)
            _, _losses = self._train(bs, _batch)

            if num_loss_item is None:
                # init
                num_loss_item = len(_losses)
                losses = [0.] * num_loss_item
                val_losses = [0.] * num_loss_item

            for i in range(num_loss_item):
                losses[i] += (_losses[i].item() * bs)

            self.optimizer.zero_grad()
            _loss = _losses[0]
            for _l in range(1, num_loss_item):
                _loss += _losses[_l]
            _loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model_params, max_norm=1.0)
            self.optimizer.step()

        for i in range(num_loss_item):
            losses[i] /= len(train_dl.dataset)

        # --- val --- #

        if val_dl is not None:
            self._set_eval()

            with torch.no_grad():
                pbar = tqdm(val_dl, leave=False) if use_pbar else val_dl

                for batch in pbar:
                    bs, _batch = self.batch_to(batch, self.device)
                    _, _val_losses = self._train(bs, _batch)

                    for i in range(num_loss_item):
                        val_losses[i] += (_val_losses[i].item() * bs)

            for i in range(num_loss_item):
                val_losses[i] /= len(val_dl.dataset)

            self._set_train()

        return losses, val_losses

    def inference(
        self,
        test_dl: DataLoader,
        get_tensor: bool = True,
        use_pbar: bool = True,
        #
        undo_norm_hldr: Callable = None,
        scale: torch.Tensor = None,
    ):
        batch: torch.Tensor
        _losses: torch.Tensor
        _preds: List[torch.Tensor | np.ndarray]
        preds: List[torch.Tensor | np.ndarray]

        self._set_eval()

        num_loss_item = None
        losses = []

        num_pred_item = None
        preds = []

        # --- test --- #

        _cls = torch.inference_mode
        # _cls = torch.no_grad

        with _cls():
            pbar = tqdm(test_dl, leave=False) if use_pbar else test_dl

            for batch in pbar:
                bs, _batch = self.batch_to(batch, self.device)
                _preds, _losses = self._inference(
                    bs,
                    _batch,
                    undo_norm_hldr=undo_norm_hldr,
                    scale=scale,
                )

                if num_loss_item is None:
                    # init
                    num_loss_item = len(_losses)
                    losses = [0.] * num_loss_item

                for i in range(num_loss_item):
                    losses[i] += (_losses[i].item() * bs)

                if num_pred_item is None:
                    # init
                    num_pred_item = len(_preds)
                    preds = [None] * num_pred_item

                for i in range(num_pred_item):
                    v = _preds[i].clone().detach()

                    if not get_tensor:
                        v = _preds[i].cpu().numpy()

                    if preds[i] is None:
                        preds[i] = v
                    else:
                        if not get_tensor:
                            preds[i] = np.concatenate((preds[i], v), axis=0)
                        else:
                            preds[i] = torch.cat((preds[i], v), dim=0)

            for i in range(num_loss_item):
                losses[i] /= len(test_dl.dataset)

        return preds, losses


# --- #


class Pipeline_Denoising(Pipeline):

    model: TrajGen
    model_handler: TrajGen
    scheduler: DDPM | DDIM

    def __init__(
        self,
        batch_to,
        model,
        optimizer_kwargs,
        scheduler: DDPM | DDIM,
    ):
        super().__init__(batch_to, model, optimizer_kwargs)

        self.scheduler = scheduler
        return

    def _train(self, batch_size: int, batch: List[torch.Tensor]):
        _size = (batch_size, )

        enc_args = batch[:-2]
        _f, _fm = batch[-2:]

        #

        noise_level = self.scheduler.get_sample_fn()(
            0,
            self.scheduler.num_timesteps,
            _size,
            dtype=torch.int64,
            device=self.device,
        )
        n_noise = get_noise_like(_f)
        _f_noisy = self.scheduler.add_noise(_f, n_noise, noise_level)

        pred_noise = self.model(*enc_args, noise_level, _f_noisy, _fm)

        #

        noise_loss = torch_mse(pred_noise, n_noise, _fm)
        return (pred_noise, ), (noise_loss, )

    def _inference(
        self,
        batch_size: int,
        batch: List[torch.Tensor],
        use_pbar: bool = False,
        #
        undo_norm_hldr: Callable = None,
        scale: torch.Tensor = None,
    ):
        _size = (batch_size, )

        enc_args = batch[:-2]
        _f, _fm = batch[-2:]

        #

        _fp = get_noise_like(_f)
        ctx = self.model_handler.forward_encoder(*enc_args)

        _pbar = self.scheduler.get_timesteps()
        pbar = tqdm(_pbar, leave=False) if use_pbar else _pbar

        for t in pbar:
            # t
            noise_level = torch.full(
                _size,
                t,
                dtype=torch.int64,
                device=self.device,
            )

            # model pred
            pred_noise = self.model_handler.forward_decoder(
                noise_level,
                _fp,
                _fm,
                ctx,
            )

            # x_{t} -> x_{t-1}
            _, _, _, _fp = self.scheduler.step(
                _fp,
                pred_noise,
                noise_level,
                get_noise_like_fn=get_noise_like,
            )

        #

        recon_loss = torch_mse(_fp, _f, _fm)

        _loss = (recon_loss, )
        if undo_norm_hldr is not None:
            f_ori = undo_norm_hldr(_f, _fm)
            fp_ori = undo_norm_hldr(_fp, _fm)

            scale = scale.to(device=self.device)
            _errors = torch_error(fp_ori, f_ori, _fm, scale)
            _loss = (recon_loss, *_errors)

        return (_fp, ), _loss


class Pipeline_FM(Pipeline):

    model: TrajGen
    model_handler: TrajGen
    scheduler: FlowMatching

    def __init__(
        self,
        batch_to,
        model,
        optimizer_kwargs,
        scheduler: FlowMatching,
    ):
        super().__init__(batch_to, model, optimizer_kwargs)

        self.scheduler = scheduler
        return

    def _train(self, batch_size: int, batch: List[torch.Tensor]):
        _size = (batch_size, )

        enc_args = batch[:-2]
        _f, _fm = batch[-2:]

        #

        noise_level = self.scheduler.get_sample_fn()(_size, device=self.device)
        n_noise = get_noise_like(_f)
        _f_noisy = self.scheduler.add_noise(_f, n_noise, noise_level)

        n_v = _f - n_noise

        pred_v = self.model(*enc_args, noise_level, _f_noisy, _fm)

        #

        v_loss = torch_mse(pred_v, n_v, _fm)
        return (pred_v, ), (v_loss, )

    def _inference(
        self,
        batch_size: int,
        batch: List[torch.Tensor],
        use_pbar: bool = False,
        #
        undo_norm_hldr: Callable = None,
        scale: torch.Tensor = None,
    ):
        _size = (batch_size, )

        enc_args = batch[:-2]
        _f, _fm = batch[-2:]

        #

        _fp = get_noise_like(_f)
        ctx = self.model_handler.forward_encoder(*enc_args)

        _pbar = self.scheduler.get_timesteps()
        pbar = tqdm(_pbar, leave=False) if use_pbar else _pbar

        dt = 1.0 / self.scheduler.num_inference_steps
        _dt = torch.full(_size, dt, device=self.device)

        for t in pbar:
            # t
            _t = torch.full(_size, t, device=self.device)

            # x_{t} -> x_{t-1}
            _fp = self.scheduler.step(
                _fp,
                _t,
                _dt,
                self.model_handler.forward_decoder,
                _fm,
                ctx,
            )

        #

        recon_loss = torch_mse(_fp, _f, _fm)

        _loss = (recon_loss, )
        if undo_norm_hldr is not None:
            f_ori = undo_norm_hldr(_f, _fm)
            fp_ori = undo_norm_hldr(_fp, _fm)

            scale = scale.to(device=self.device)
            _errors = torch_error(fp_ori, f_ori, _fm, scale)
            _loss = (recon_loss, *_errors)

        return (_fp, ), _loss
