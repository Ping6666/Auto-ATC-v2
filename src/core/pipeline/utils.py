import torch


def torch_mse(pred: torch.Tensor, gt: torch.Tensor, mask: torch.Tensor):
    """
    Args:
        pred: with shape (B, S, T, F) or (B, T, F)
        gt:   with shape (B, S, T, F) or (B, T, F)
        mask: with shape (B, S, T)    or (B, T)
    """
    # (B, S, T, F) or (B, T, F)
    _loss = (pred - gt)**2
    # (B, S, T, 1) or (B, T, 1)
    _mask = (~mask).float().unsqueeze(dim=-1)

    loss_sum = (_loss * _mask).sum()
    mask_count = _mask.sum()

    if mask_count == 0:
        return torch.zeros_like(loss_sum)
    return loss_sum / mask_count


def torch_error(
    pred: torch.Tensor,
    gt: torch.Tensor,
    mask: torch.Tensor,
    scale: torch.Tensor,
):
    """
    Args:
        pred: with shape (B, S, T, F) or (B, T, F)
        gt:   with shape (B, S, T, F) or (B, T, F)
        mask: with shape (B, S, T)    or (B, T)
    """
    # (B, S, T, F) or (B, T, F)
    _error = abs(pred - gt)
    # (B, S, T, 1) or (B, T, 1)
    _mask = (~mask).float().unsqueeze(dim=-1)

    reduce_dims = list(range(_error.ndim - 1))
    error_sum = (_error * _mask).sum(dim=reduce_dims)
    mask_count = _mask.sum(dim=reduce_dims)

    if mask_count == 0:
        z = torch.zeros_like(error_sum)
        zs = torch.unbind(z, dim=-1)
        return *zs, zs[0].clone()

    _error_pow = (_error * _mask * scale)**2
    dist_error = torch.sqrt(_error_pow.sum(dim=-1, keepdim=True))
    dist_error_sum = dist_error.sum(dim=reduce_dims)

    zs = torch.unbind(error_sum / mask_count, dim=-1)
    return *zs, (dist_error_sum / mask_count).squeeze()
