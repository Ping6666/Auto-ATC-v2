"""
ref
1. https://github.com/huggingface/diffusers/blob/v0.29.0/src/diffusers/schedulers/scheduling_ddpm.py#L129
2. https://github.com/sillsill777/Diffusion/blob/master/src/diffusion.py
3. https://github.com/tcapelle/Diffusion-Models-pytorch/blob/main/ddpm_conditional.py
4. https://github.com/dome272/Diffusion-Models-pytorch/blob/main/ddpm_conditional.py
5. https://github.com/yang-song/score_sde/blob/main/models/utils.py#L164
"""

from typing import Callable

import torch

from core.utils import get_tensor_like
from core.diffuser.module import SchedulerMixin


class DDPM(SchedulerMixin):

    def __init__(
        self,
        device: torch.device,
        num_timesteps: int = 1000,
        beta_start: float = 0.0001,
        beta_end: float = 0.02,
        clip: bool = True,
        x0_clip: float = 1.0,
    ):
        """
        ref.: https://arxiv.org/pdf/2006.11239
        """

        super().__init__()

        self.device = device
        self.num_timesteps = num_timesteps
        self.beta_start = beta_start
        self.beta_end = beta_end
        self.clip = clip
        self.x0_clip = x0_clip

        # --- var -- #

        self.betas = torch.linspace(self.beta_start,
                                    self.beta_end,
                                    self.num_timesteps,
                                    dtype=torch.float64,
                                    device=self.device)
        # (a1, a2, a3, ..., at)
        self.alphas = 1. - self.betas
        # (a1, a1*a2, a1*a2*a3, ..., a1*a2*...*at)
        self.alphas_cumprod = torch.cumprod(self.alphas, dim=0)
        # (1, a1, a1*a2, ..., a1*a2*...*a(t-1))
        self.alphas_cumprod_prev = torch.roll(self.alphas_cumprod, 1, dims=0)
        self.alphas_cumprod_prev[0] = 1.

        #
        # for q(x_t | x_0)

        self.q_x0_coef = torch.sqrt(self.alphas_cumprod)
        self.q_noise_coef = torch.sqrt(1. - self.alphas_cumprod)

        #
        # for p(x_{t-1} | x_t, x_0)

        self.p_clip_xt_coef = torch.sqrt(1. / self.alphas_cumprod)
        self.p_clip_noise_coef = torch.sqrt((1. / self.alphas_cumprod) - 1.)

        self.p_tilde_x0_coef = (self.betas *
                                torch.sqrt(self.alphas_cumprod_prev) /
                                (1. - self.alphas_cumprod))
        self.p_tilde_xt_coef = (torch.sqrt(self.alphas) *
                                (1. - self.alphas_cumprod_prev) /
                                (1. - self.alphas_cumprod))

        self.p_no_clip_coef = torch.sqrt(1. / self.alphas)
        self.p_no_clip_noise_coef = (self.betas /
                                     torch.sqrt(1. - self.alphas_cumprod))

        self.p_tilde_betas = (self.betas * ((1. - self.alphas_cumprod_prev) /
                                            (1. - self.alphas_cumprod)))

        return

    def get_sample_fn(self):
        # uniformly
        return torch.randint

    def get_timesteps(self):
        return range(self.num_timesteps)[::-1]

    # --- Diffusion --- #

    def add_noise(
        self,
        x0: torch.Tensor,
        noise: torch.Tensor,
        t: torch.IntTensor,
    ):
        """
        Diffusion (forward process)
        which is q(x_t | x_0)

        """

        _q_x0_coef = get_tensor_like(self.q_x0_coef[t], x0)
        _q_noise_coef = get_tensor_like(self.q_noise_coef[t], x0)

        x0 = x0.to(torch.float64)
        noise = noise.to(torch.float64)

        # formula (2) & formula (4)
        xt = _q_x0_coef * x0 + _q_noise_coef * noise

        xt = xt.to(torch.float32)
        return xt

    # --- Denoising --- #

    def step(
        self,
        xt: torch.Tensor,
        pred_noise: torch.Tensor,
        t: torch.IntTensor,
        get_noise_like_fn: Callable[[torch.Tensor], torch.Tensor],
    ):
        """
        Denoising (reverse process)
        which is p_θ(x_{t-1} | x_t)

        Vars in this fn.:
            x0: x_{0}, xt: x_{t}, xt_1: x_{t-1}

        """

        _p_clip_xt_coef = get_tensor_like(self.p_clip_xt_coef[t], xt)
        _p_clip_n_coef = get_tensor_like(self.p_clip_noise_coef[t], xt)

        _p_tilde_x0_coef = get_tensor_like(self.p_tilde_x0_coef[t], xt)
        _p_tilde_xt_coef = get_tensor_like(self.p_tilde_xt_coef[t], xt)

        _p_no_clip_coef = get_tensor_like(self.p_no_clip_coef[t], xt)
        _p_no_clip_n_coef = get_tensor_like(self.p_no_clip_noise_coef[t], xt)

        _p_tilde_betas = get_tensor_like(self.p_tilde_betas[t], xt)

        xt = xt.to(torch.float64)
        pred_noise = pred_noise.to(torch.float64)

        #

        x0 = _p_clip_xt_coef * xt - _p_clip_n_coef * pred_noise

        if self.clip:
            # formula (15)
            x0 = x0.clamp(-self.x0_clip, self.x0_clip)

            # formula (7)
            mean = _p_tilde_x0_coef * x0 + _p_tilde_xt_coef * xt

        else:
            # formula (11)
            mean = _p_no_clip_coef * (xt - _p_no_clip_n_coef * pred_noise)

        variance = torch.sqrt(_p_tilde_betas) * get_noise_like_fn(xt)
        variance = variance.masked_fill(
            get_tensor_like(t <= 0, variance),
            0.,
        )

        xt_1 = mean + variance

        mean = mean.to(torch.float32)
        variance = variance.to(torch.float32)
        xt_1 = xt_1.to(torch.float32)

        return x0, mean, variance, xt_1
