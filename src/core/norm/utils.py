import numpy as np
import torch


def valid_check(v: np.ndarray | torch.Tensor):
    if isinstance(v, np.ndarray):
        assert not np.any(np.isnan(v))
        assert not np.any(np.isinf(v))
    elif isinstance(v, torch.Tensor):
        assert not torch.isnan(v).any()
        assert not torch.isinf(v).any()
    else:
        raise NotImplementedError
    return
