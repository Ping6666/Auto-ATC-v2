from typing import Dict, List, Tuple

from tqdm import tqdm
import numpy as np
import torch


class Norm():

    norm: Dict[str, Tuple[float, float]]

    def __init__(self):
        return

    def _do_norm(self):
        raise NotImplementedError

    def _undo_norm(self):
        raise NotImplementedError

    def do_norm_workhouse(
        self,
        x: np.ndarray | torch.Tensor,
        m: np.ndarray | torch.Tensor,
        features: List[str],
        do_copy: bool = True,
    ):
        if do_copy:
            if isinstance(x, np.ndarray):
                x_norm = x.copy()
            elif isinstance(x, torch.Tensor):
                x_norm = x.clone()
        else:
            x_norm = x

        for i, f in enumerate(tqdm(features)):
            if f not in self.norm.keys():
                continue
            x_norm[..., i] = self._do_norm(f, x_norm[..., i], m)
        return x_norm

    def undo_norm_workhouse(
        self,
        x: np.ndarray | torch.Tensor,
        m: np.ndarray | torch.Tensor,
        features: List[str],
        do_copy: bool = True,
    ):
        if do_copy:
            if isinstance(x, np.ndarray):
                x_ori = x.copy()
            elif isinstance(x, torch.Tensor):
                x_ori = x.clone()
        else:
            x_ori = x

        for i, f in enumerate(tqdm(features)):
            if f not in self.norm.keys():
                continue
            x_ori[..., i] = self._undo_norm(f, x_ori[..., i], m)
        return x_ori
