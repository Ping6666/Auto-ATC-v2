from typing import Dict

import torch

from core.utils import get_dict_len


def single_batch_to(
    batch: Dict[str, torch.Tensor] | Dict[str, Dict[str, torch.Tensor]],
    device: torch.device,
):
    bs = get_dict_len(batch)
    _batch = (
        {
            k: v.to(device)
            for k, v in batch['i'].items()
        },
        batch['im'].to(device),
        batch['o'].to(device),
        batch['om'].to(device),
        batch['p'].to(device),
        batch['pm'].to(device),
        batch['f'].to(device),
        batch['fm'].to(device),
    )
    return bs, _batch
