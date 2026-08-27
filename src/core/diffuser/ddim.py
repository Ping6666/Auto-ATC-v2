"""
ref
1. https://github.com/huggingface/diffusers/blob/v0.29.0/src/diffusers/schedulers/scheduling_ddim.py#L131
"""

from typing import Callable

import torch

from core.utils import get_tensor_like
from core.diffuser.module import SchedulerMixin


class DDIM(SchedulerMixin):

    def __init__(
        self,
        device: torch.device,
        num_timesteps: int = 1000,
        num_inference_steps: int = 50,  # 50, 500
        beta_start: float = 0.0001,
        beta_end: float = 0.02,
        clip: bool = True,
        x0_clip: float = 1.0,
        #
        # 0.0, 1.0
        eta: float = 0.0,
    ):
        """
        ref.: https://arxiv.org/pdf/2010.02502
        """

        super().__init__()

        self.device = device
        self.num_timesteps = num_timesteps
        self.num_inference_steps = num_inference_steps
        self.beta_start = beta_start
        self.beta_end = beta_end
        self.clip = clip
        self.x0_clip = x0_clip
        self.eta = eta

        # --- var -- #

        if not 1 <= self.num_inference_steps <= self.num_timesteps:
            raise ValueError

        if self.num_inference_steps == 1:
            self.timesteps = torch.tensor(
                [self.num_timesteps - 1],
                dtype=torch.int64,
                device=self.device,
            )
        else:
            self.timesteps = torch.linspace(
                0,
                self.num_timesteps - 1,
                self.num_inference_steps,
                dtype=torch.float64,
                device=self.device,
            ).round().to(torch.int64)

        self.previous_timesteps = torch.full(
            (self.num_timesteps, ),
            -1,
            dtype=torch.int64,
            device=self.device,
        )
        self.previous_timesteps[self.timesteps[1:]] = self.timesteps[:-1]

        self.betas = torch.linspace(
            self.beta_start,
            self.beta_end,
            self.num_timesteps,
            dtype=torch.float64,
            device=self.device,
        )
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

        return

    def get_sample_fn(self):
        # uniformly
        return torch.randint

    def get_timesteps(self):
        return self.timesteps.flip(0).tolist()

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
            x0: x_{0}
            xt: x_{t}
            xt_1: x_{t-1}

        Args:
            xt:         (B, S, F)
            pred_noise: (B, S, F)
            t:          (B)

        """

        _p_clip_xt_coef = get_tensor_like(self.p_clip_xt_coef[t], xt)
        _p_clip_n_coef = get_tensor_like(self.p_clip_noise_coef[t], xt)

        xt = xt.to(torch.float64)
        pred_noise = pred_noise.to(torch.float64)

        #

        x0 = _p_clip_xt_coef * xt - _p_clip_n_coef * pred_noise

        if self.clip:
            x0 = x0.clamp(-self.x0_clip, self.x0_clip)

        # --- mimic function --- #
        # self.p_tilde_betas = (self.betas * ((1. - self.alphas_cumprod_prev) /
        #                                     (1. - self.alphas_cumprod)))

        t_1_raw = self.previous_timesteps[t]

        _ac2 = get_tensor_like(self.alphas_cumprod[t], xt)
        _acp2 = get_tensor_like(self.alphas_cumprod[t_1_raw.clamp_min(0)], xt)

        _t_1 = get_tensor_like(t_1_raw, xt)
        _acp2 = torch.where(_t_1 >= 0, _acp2, 1.)
        _acp = torch.sqrt(_acp2)

        # beta
        _beta = 1. - _acp2

        # alphas cumprod ratio
        _ac_ratio = _ac2 / torch.clamp(_acp2, min=1e-12)

        _sigma_core = ((_beta * torch.clamp(1. - _ac_ratio, min=0.)) /
                       torch.clamp(1. - _ac2, min=1e-12))

        sigma2 = torch.clamp((self.eta * self.eta) * _sigma_core, min=0.)
        sigma = torch.sqrt(sigma2)

        _dir = torch.sqrt(torch.clamp(1. - _acp2 - sigma2, min=0.))
        mean = _acp * x0 + _dir * pred_noise

        #

        variance = sigma * get_noise_like_fn(xt)
        variance = variance.masked_fill(
            get_tensor_like(t <= 0, variance),
            0.,
        )

        xt_1 = mean + variance

        mean = mean.to(torch.float32)
        variance = variance.to(torch.float32)
        xt_1 = xt_1.to(torch.float32)

        return x0, mean, variance, xt_1
