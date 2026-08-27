from typing import Dict, Optional
from copy import deepcopy
import logging

from torch.utils.data import Dataset, DataLoader
from torch.utils.data.distributed import DistributedSampler
from torch.nn.parallel import DistributedDataParallel as DDP
import numpy as np
import torch

from core.const import IN_FEATURES, OUT_FEATURES, OUT_SHIFT_FEATURES
from core.config import SampleConfig, Config
from core.diffuser import DDPM, DDIM, FlowMatching
from core.model import TrajGen_Single, TrajGen_Multi
from core.pipeline import Pipeline_Denoising, Pipeline_FM, single_batch_to, multi_batch_to


def make_dataloader(dataset: Dataset, batch_size, shuffle: bool = True):
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
    )
    return loader


def make_ddp_dataloader(
    dataset: Dataset,
    num_replicas,
    rank,
    seed,
    batch_size,
    shuffle: bool = True,
):
    sampler = DistributedSampler(
        dataset,
        num_replicas=num_replicas,
        rank=rank,
        shuffle=shuffle,
        seed=seed,
    )
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        sampler=sampler,
        pin_memory=True,
    )
    return sampler, loader


# --- #


def get_L_04_model_kwargs():
    kwargs = dict(
        d_model=64,
        brain_d_model=64,
        nhead=4,
        widening_factor=16,
        enc_num_layers=4,
        brain_num_layers=4,
        dec_num_layers=4,
        dropout=0.,
    )
    return kwargs


def get_L_06_model_kwargs():
    kwargs = dict(
        d_model=64,
        brain_d_model=64,
        nhead=4,
        widening_factor=16,
        enc_num_layers=6,
        brain_num_layers=6,
        dec_num_layers=6,
        dropout=0.,
    )
    return kwargs


def get_L_08_model_kwargs():
    kwargs = dict(
        d_model=64,
        brain_d_model=64,
        nhead=4,
        widening_factor=16,
        enc_num_layers=8,
        brain_num_layers=8,
        dec_num_layers=8,
        dropout=0.,
    )
    return kwargs


def get_x_on_kwargs():
    kwargs = dict(use_x_atten=True)
    return kwargs


def get_x_off_kwargs():
    kwargs = dict(use_x_atten=False)
    return kwargs


def get_t_only_kwargs():
    kwargs = dict(future_attn_mode='t_only')
    return kwargs


def get_t_s_mixed_kwargs():
    kwargs = dict(future_attn_mode='t_s_mixed')
    return kwargs


def get_1e_minus_3_opt_kwargs():
    kwargs = dict(
        lr=1e-3,
        weight_decay=1e-2,
    )
    return kwargs


def get_1e_minus_4_opt_kwargs():
    kwargs = dict(
        lr=1e-4,
        weight_decay=1e-2,
    )
    return kwargs


def get_3e_minus_4_opt_kwargs():
    kwargs = dict(
        lr=3e-4,
        weight_decay=1e-2,
    )
    return kwargs


KWARGS = {
    #
    'L_04': get_L_04_model_kwargs,
    'L_06': get_L_06_model_kwargs,
    'L_08': get_L_08_model_kwargs,
    #
    'x_on': get_x_on_kwargs,
    'x_off': get_x_off_kwargs,
    't_only': get_t_only_kwargs,
    't_s_mixed': get_t_s_mixed_kwargs,
    #
    # --- #
    #
    'opt_1e-3': get_1e_minus_3_opt_kwargs,
    'opt_1e-4': get_1e_minus_4_opt_kwargs,
    'opt_3e-4': get_3e_minus_4_opt_kwargs,
    #
}


def get_optimizer_kwargs(cfg: Config):
    opt_keys = cfg.opt_key_nargs

    _dict = dict()
    for k in opt_keys:
        _dict.update(KWARGS[k]())
    return _dict


def make_model(s_cfg: SampleConfig, cfg: Config):
    future_n_features = -1
    if cfg.out_mode == 'original':
        future_n_features = len(OUT_FEATURES)
    elif cfg.out_mode == 'shift':
        future_n_features = len(OUT_SHIFT_FEATURES)
    else:
        raise NotImplementedError

    model_cls = None
    if s_cfg.mode == 'single':
        model_cls = TrajGen_Single
        _dict = dict(
            icao=s_cfg.icao,
            num_aircraft=s_cfg.max_num_aircraft,
            past_len=s_cfg.past_len,
            past_n_features=len(IN_FEATURES),
            future_len=s_cfg.future_len,
            future_n_features=future_n_features,
        )
    elif s_cfg.mode == 'multiple':
        model_cls = TrajGen_Multi
        _dict = dict(
            icao=s_cfg.icao,
            num_aircraft=s_cfg.max_num_aircraft,
            past_len=s_cfg.past_len,
            past_n_features=len(IN_FEATURES),
            future_len=s_cfg.future_len,
            future_n_features=future_n_features,
        )
    else:
        raise NotImplementedError

    model_keys = cfg.model_key_nargs
    for k in model_keys:
        _dict.update(KWARGS[k]())

    if s_cfg.mode == 'single':
        _dict.pop('brain_num_layers')
        _dict.pop('brain_d_model')

    model = model_cls(**_dict)
    return model


def wrap_ddp_model(model: torch.nn.Module, device: torch.device):
    device = torch.device(device)

    if device.type == 'cuda':
        device_index = device.index
        if device_index is None:
            device_index = torch.cuda.current_device()
        return DDP(
            model,
            device_ids=[device_index],
            output_device=device_index,
        )
    return DDP(model)


def make_pipeline(
    s_cfg: SampleConfig,
    cfg: Config,
    device: torch.device,
    logger: Optional[logging.Logger] = None,
    use_ddp: bool = False,
):
    _s_cfg = None
    if cfg.out_mode == 'original':
        _s_cfg = s_cfg
    elif cfg.out_mode == 'shift':
        _s_cfg = deepcopy(s_cfg)
        _s_cfg.future_len -= 1
    else:
        raise NotImplementedError

    model = make_model(_s_cfg, cfg).to(device)

    if logger is not None:
        logger.info(f"{model}")
        if _s_cfg.mode == 'multiple':
            logger.info(f"{model.future_attn_mode = }")
            logger.info(f"{model.brain_d_model = }")

    if use_ddp:
        model = wrap_ddp_model(model, device)

    optimizer_kwargs = get_optimizer_kwargs(cfg)
    if logger is not None:
        logger.info(f"{optimizer_kwargs}")

    batch_to_fn = None
    if _s_cfg.mode == 'single':
        batch_to_fn = single_batch_to
    elif _s_cfg.mode == 'multiple':
        batch_to_fn = multi_batch_to
    else:
        raise NotImplementedError

    scheduler_cls = None
    pipeline_cls = None
    if cfg.diffuser == 'ddpm':
        scheduler_cls = DDPM
        pipeline_cls = Pipeline_Denoising
    elif cfg.diffuser == 'ddim':
        scheduler_cls = DDIM
        pipeline_cls = Pipeline_Denoising
    elif cfg.diffuser == 'fm':
        scheduler_cls = FlowMatching
        pipeline_cls = Pipeline_FM
    else:
        raise NotImplementedError

    pipeline = pipeline_cls(
        batch_to_fn,
        model,
        optimizer_kwargs,
        scheduler_cls(device),
    )
    return pipeline


def make_dataset(mode: str, out_mode: str, ds: Dict[str, np.ndarray]):
    f, fm = None, None
    if out_mode == 'original':
        f = ds['f']
        fm = ds['fm']
    elif out_mode == 'shift':
        f = ds['fs']
        fm = ds['fsm']
    else:
        raise NotImplementedError

    _ds = dict(
        i=ds['i'],
        p=ds['p'],
        pm=ds['pm'],
        fa=ds['fa'],
        fam=ds['fam'],
        f=f,
        fm=fm,
    )
    if mode == 'single':
        _ds['im'] = ds['im']
        _ds['o'] = ds['o']
        _ds['om'] = ds['om']
    elif mode == 'multiple':
        _ds['xyz'] = ds['xyz']
    else:
        raise NotImplementedError
    return _ds
