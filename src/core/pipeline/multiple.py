from typing import Dict

import torch

from core.utils import get_dict_len


def multi_batch_to(
    batch: Dict[str, torch.Tensor] | Dict[str, Dict[str, torch.Tensor]],
    device: torch.device,
):
    bs = get_dict_len(batch)
    _batch = (
        batch['xyz'].to(device),
        {
            k: v.to(device)
            for k, v in batch['i'].items()
        },
        batch['p'].to(device),
        batch['pm'].to(device),
        batch['f'].to(device),
        batch['fm'].to(device),
    )
    return bs, _batch
