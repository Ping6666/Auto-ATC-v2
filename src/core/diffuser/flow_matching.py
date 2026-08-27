import torch

from core.utils import get_tensor_like
from core.diffuser.module import SchedulerMixin


class FlowMatching(SchedulerMixin):

    def __init__(
        self,
        device: torch.device,
        num_inference_steps: int = 50,
        mode: str = 'heun',
    ):
        super().__init__()
        self.device = device
        self.num_inference_steps = num_inference_steps
        self.mode = mode

        # 0->1 (noise to data)
        self.timesteps = torch.linspace(
            0.,
            1. - (1. / self.num_inference_steps),
            self.num_inference_steps,
            device=self.device,
        )
        return

    def get_sample_fn(self):
        return torch.rand

    def get_timesteps(self):
        return self.timesteps.tolist()

    def add_noise(
        self,
        x0: torch.Tensor,
        noise: torch.Tensor,
        t: torch.Tensor,
    ):
        """
        Flow Matching forward

        x_t = (1 - t) * noise + t * x0
            noise: Noise (Gaussian)
        """

        t = get_tensor_like(t, x0)

        x0 = x0.to(torch.float64)
        noise = noise.to(torch.float64)

        xt = (1. - t) * noise + t * x0

        xt = xt.to(torch.float32)
        return xt

    def step(self, xt, t, dt, model_fn, *args):
        if self.mode == 'euler':
            return self._step_euler(xt, t, dt, model_fn, *args)
        elif self.mode == 'heun':
            return self._step_heun(xt, t, dt, model_fn, *args)

        raise NotImplementedError

    def _step_euler(self, xt, t, dt, model_fn, *args):
        """
        Euler's Method (1st Order)
        """
        _dt = get_tensor_like(dt, xt)

        v1 = model_fn(t, xt, *args)

        xt_1 = xt + v1 * _dt
        return xt_1

    def _step_heun(self, xt, t, dt, model_fn, *args):
        """
        Heun's Method (2nd Order)
        """
        _dt = get_tensor_like(dt, xt)

        v1 = model_fn(t, xt, *args)
        _xt_1 = xt + v1 * _dt

        t_1 = t + dt
        v2 = model_fn(t_1, _xt_1, *args)

        xt_1 = xt + 0.5 * _dt * (v1 + v2)
        return xt_1
