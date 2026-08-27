from typing import Dict, Tuple

import numpy as np
import torch

from core.norm.module import Norm
from core.norm.utils import valid_check


class MeanStdNorm(Norm):

    # [_name] -> (mean, std)
    norm: Dict[str, Tuple[float, float]]

    def __init__(self):
        super().__init__()

        self.norm = {}

        # self.norm_mean = 0
        # self.norm_std = 1
        return

    def register(self, _name: str, data: np.ndarray):
        """
        Args:
            data: with shape (..., F)
            mask: for transformer with shape (...)
        """
        assert _name not in self.norm.keys()
        self.norm[_name] = (float(data.mean()), float(data.std()))
        # print(f"MeanStdNorm.register | {_name} {self.norm[_name]}")
        return

    def _do_norm(
        self,
        _name: str,
        data: np.ndarray | torch.Tensor,
        mask: np.ndarray | torch.Tensor,
    ):
        valid_check(data)
        valid_check(mask)
        assert _name in self.norm.keys()

        _mean, _std = self.norm[_name]
        data[~mask] = (data[~mask] - _mean) / (_std + 1e-8)

        valid_check(data)
        return data

    def _undo_norm(
        self,
        _name: str,
        data: np.ndarray | torch.Tensor,
        mask: np.ndarray | torch.Tensor,
    ):
        valid_check(data)
        valid_check(mask)
        assert _name in self.norm.keys()

        _mean, _std = self.norm[_name]
        data[~mask] = (data[~mask] * _std) + _mean

        valid_check(data)
        return data
