from typing import Dict

from torch.utils.data import Dataset
import numpy as np
import torch

from core.utils import get_dict_len


class PackedDataset(Dataset):

    data: torch.Tensor

    def __init__(self, data: np.ndarray):
        super().__init__()

        self.data = torch.tensor(data)

        self.data_len = len(data)
        return

    def __len__(self) -> int:
        return self.data_len

    def __getitem__(self, idx):
        return self.data[idx]


class PackedDictDataset(Dataset):

    data: Dict[str, torch.Tensor]

    def __init__(self, data: Dict[str, np.ndarray]):
        super().__init__()

        self.data = {}
        for k, v in data.items():
            self.data[k] = torch.tensor(v)

        self.data_len = get_dict_len(data)
        return

    def __len__(self) -> int:
        return self.data_len

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.data.items()}


class PackedDictDictDataset(Dataset):

    data: Dict[str, torch.Tensor] | Dict[str, Dict[str, torch.Tensor]]

    def __init__(self, data: Dict[str, np.ndarray]):
        super().__init__()

        self.data = {}
        for k1, v1 in data.items():
            if isinstance(v1, Dict):
                self.data[k1] = {}
                for k2, v2 in v1.items():
                    self.data[k1][k2] = torch.tensor(v2)
            else:
                self.data[k1] = torch.tensor(v1)

        self.data_len = get_dict_len(data)
        return

    def __len__(self) -> int:
        return self.data_len

    def __getitem__(self, idx):
        _item = {}
        for k1, v1 in self.data.items():
            if isinstance(v1, Dict):
                _item[k1] = {}
                for k2, v2 in v1.items():
                    _item[k1][k2] = v2[idx]
            else:
                _item[k1] = v1[idx]
        return _item
