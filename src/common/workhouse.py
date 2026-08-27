from typing import Dict
from copy import deepcopy
import pathlib

import torch

from core.utils import mkdir
from core.config import SampleConfig, PackConfig, Config
from core.norm import MinMaxNorm, MeanStdNorm
from core.factory import make_pipeline

# --- ckpt --- #


def save_ckpt_workhouse(ckpt: Dict, ckpt_fname: str):
    ckpt_path = pathlib.Path(ckpt_fname).absolute()

    _folder = str(ckpt_path.parent)
    _ckpt_fname = str(ckpt_path)

    mkdir(_folder, can_exists=True)
    torch.save(ckpt, _ckpt_fname)

    print(f"save_ckpt_workhouse: {_ckpt_fname} SAVED!")
    return


def load_ckpt_workhouse(ckpt_fname: str, device: torch.device = 'cpu'):
    # ckpt = {
    #     "sample_config": s_cfg,
    #     "pack_config": p_cfg,
    #     "config": cfg,
    #     "min_max_norm": mmn,
    #     "mean_std_norm": msn,
    #     "model": pipeline.model_handler.state_dict(),
    #     "optimizer": pipeline.optimizer.state_dict(),
    # }

    torch.serialization.add_safe_globals([SampleConfig, PackConfig, Config])
    torch.serialization.add_safe_globals([MinMaxNorm, MeanStdNorm])

    state_dict = torch.load(ckpt_fname, map_location=device, weights_only=True)
    s_cfg: SampleConfig = state_dict['sample_config']
    p_cfg: PackConfig = state_dict['pack_config']
    cfg: Config = state_dict['config']
    mmn: MinMaxNorm = state_dict['min_max_norm']
    msn: MeanStdNorm = state_dict['mean_std_norm']

    #

    pipeline = make_pipeline(s_cfg, cfg, device)

    pipeline.model.load_state_dict(state_dict["model"])
    pipeline._set_eval()
    pipeline.optimizer.load_state_dict(state_dict["optimizer"])

    print(f"load_ckpt_workhouse: {ckpt_fname} SUCCESSFUL!")
    return s_cfg, p_cfg, cfg, mmn, msn, pipeline
