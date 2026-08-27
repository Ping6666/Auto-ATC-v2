from typing import Dict, Tuple

import numpy as np
import torch

from core.norm.module import Norm
from core.norm.utils import valid_check


class MinMaxNorm(Norm):

    # [_name] -> (min, max)
    norm: Dict[str, Tuple[float, float]]

    def __init__(self):
        super().__init__()

        self.norm = {}

        self.norm_min = -1
        self.norm_max = 1
        return

    def register(self, _name: str, data: np.ndarray):
        """
        Args:
            data: with shape (..., F)
            mask: for transformer with shape (...)
        """
        assert _name not in self.norm.keys()
        self.norm[_name] = (float(data.min()), float(data.max()))
        # print(f"MinMaxNorm.register | {_name} {self.norm[_name]}")
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

        _min, _max = self.norm[_name]
        data[~mask] = ((data[~mask] - _min) / (_max - _min) *
                       (self.norm_max - self.norm_min) + self.norm_min)

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

        _min, _max = self.norm[_name]
        data[~mask] = ((data[~mask] - self.norm_min) /
                       (self.norm_max - self.norm_min) * (_max - _min) + _min)

        valid_check(data)
        return data
