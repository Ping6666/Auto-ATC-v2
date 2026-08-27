from typing import Dict, List, Optional
from math import ceil
import os, time, pathlib, random
import logging
import pickle
import json

from tqdm import tqdm
import numpy as np
import torch

T = Dict[str, np.ndarray] | Dict[str, Dict[str, np.ndarray]]

# ----- time ----- #


def get_time():
    return time.time()


def get_time_str():
    return time.strftime('%Y_%m_%d-%H_%M_%S', time.localtime())


class Timer():

    def __init__(self):
        self.start_time = None
        self.end_time = None
        return

    def start(self):
        self.start_time = get_time()
        return self.start_time

    def end(self):
        self.end_time = get_time()
        return self.end_time

    def get_time_spend(self):
        return self.end_time - self.start_time


# --- logger --- #


def create_logger(
    folder: str,
    fname: str = '#log.txt',
    is_master: bool = True,
    #
    logger_name: str = None,
):
    """
    ref. https://github.com/facebookresearch/DiT/blob/main/train.py#L67
    """
    if logger_name is None:
        logger_name = __name__

    if is_master:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(f"{folder}/{fname}")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
    else:
        logger = logging.getLogger(logger_name)
        logger.addHandler(logging.NullHandler())
    return logger


# ----- gpu ----- #


def get_gpu_status(nv_smi: bool = False, gpustat: bool = True):
    """
    NVIDIA System Management Interface
    """

    _str = "\n"
    if nv_smi:
        _str += os.popen('nvidia-smi').read().rstrip()
        _str += "\n"

    if gpustat:
        _str += os.popen('gpustat -acup').read().rstrip()
        _str += "\n"

    return _str


def get_torch_device(device_name, use_gpu: bool = True):
    _device_name = device_name

    if (use_gpu and (not torch.cuda.is_available())):
        raise AssertionError

    if ((not use_gpu) or (device_name is None)
            or (not torch.cuda.is_available())):
        _device_name = "cpu"

    device = torch.device(_device_name)
    return device


def set_torch_seeds(seed: int):
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    return


# --- os --- #


def mkdir(folder, can_exists: bool = False, verbose: bool = False):
    p = pathlib.Path(folder)

    if p.exists():
        if not can_exists:
            print(f"ERROR | mkdir folder: {folder} exists!")
            raise FileExistsError

        if verbose:
            print(f"WARNING | mkdir folder: {folder} exists!")

    p.mkdir(parents=True, exist_ok=True)
    return


def _listdir(
    folder: str,
    do_join: bool = False,
    get_file: bool = False,
    get_dir: bool = False,
):
    result = []

    _listdir = os.listdir(folder)
    for _dir in _listdir:
        _tmp = os.path.join(folder, _dir)

        _dir1 = _dir
        if do_join:
            _dir1 = _tmp

        if get_file and os.path.isfile(_tmp):
            result.append(_dir1)

        if get_dir and os.path.isdir(_tmp):
            result.append(_dir1)

    return result


def listdir(
    folder: str,
    do_join: bool = False,
    get_file: bool = False,
    get_dir: bool = False,
    level: int = -1,
):
    level = int(level)
    assert level >= -1

    result = []
    if level == -1:
        res = _listdir(
            folder,
            do_join=do_join,
            get_file=get_file,
            get_dir=get_dir,
        )
        result.extend(res)

        _folders = _listdir(
            folder,
            do_join=True,
            get_file=False,
            get_dir=True,
        )
        for f in _folders:
            res = listdir(
                f,
                do_join=do_join,
                get_file=get_file,
                get_dir=get_dir,
                level=level,
            )
            result.extend(res)

    elif level == 0:
        res = _listdir(
            folder,
            do_join=do_join,
            get_file=get_file,
            get_dir=get_dir,
        )
        result.extend(res)

    else:
        _folders = _listdir(
            folder,
            do_join=True,
            get_file=False,
            get_dir=True,
        )
        for f in _folders:
            res = listdir(
                f,
                do_join=do_join,
                get_file=get_file,
                get_dir=get_dir,
                level=level - 1,
            )
            result.extend(res)

    return result


# --- file --- #


def dump_json(_data, fname: str):
    with open(fname, 'w') as f:
        json.dump(_data, f, indent=2)
        print(f"dump_json: {fname} SAVED!")
    return


def load_json(fname: str):
    _data = None
    with open(fname, 'r') as f:
        _data = json.load(f)
        print(f"load_json: {fname} SUCCESSFUL!")
    return _data


def dump_pkl(_data, fname: str):
    with open(fname, 'wb') as f:
        pickle.dump(_data, f)
        print(f"dump_pkl: {fname} SAVED!")
    return


def load_pkl(fname: str):
    _data = None
    with open(fname, 'rb') as f:
        _data = pickle.load(f)
        print(f"load_pkl: {fname} SUCCESSFUL!")
    return _data


def dump_npy(_data, fname: str):
    with open(fname, 'wb') as f:
        np.save(f, arr=_data)
        print(f"dump_npy: {fname} SAVED!")
    return


def load_npy(fname: str, allow_pickle: bool = False):
    _data = None
    with open(fname, 'rb') as f:
        _data = np.load(f, allow_pickle=allow_pickle)
        print(f"load_npy: {fname} SUCCESSFUL!")
    return _data


# --- dataset --- #


def get_idx(l: List, k):
    if k in l:
        return l.index(k)
    # return -1
    raise KeyError


def make_list_split(
    args: np.ndarray,
    splits_ratio: List[float],
    do_shuffle: bool = True,
):
    assert np.all(np.array(splits_ratio) > 0.)

    assert abs(float(np.array(splits_ratio).sum()) - 1.0) < 1e-8

    data_len = len(args)
    indice = np.arange(data_len)

    if do_shuffle:
        np.random.shuffle(indice)

    idx = 0
    splits_size = []
    for r in splits_ratio[:-1]:
        idx += int(data_len * r)
        splits_size.append(idx)
    split_indice = np.split(indice, splits_size)

    split_args = []
    for _indice in split_indice:
        _split_args = args[_indice]
        split_args.append(_split_args)

    return split_args


def get_dict_len(args: T, batch_size: Optional[int] = None):
    """
    return the length of the dataset

    assertion check all ele. in args got same length.

    Args:
        args: a dict of List

    Return:
        the length of the dataset

    """

    data_len = -1
    for _, v1 in args.items():
        if isinstance(v1, Dict):
            for _, v2 in v1.items():
                if data_len == -1:
                    data_len = len(v2)
                elif data_len != len(v2):
                    raise AssertionError

        else:
            if data_len == -1:
                data_len = len(v1)
            elif data_len != len(v1):
                raise AssertionError

    if batch_size is None:
        return data_len

    _round = ceil(data_len / batch_size)
    return data_len, _round


def make_dict_split(
    args: T,
    splits: List[float] | List[int],
    do_shuffle: bool = True,
    #
    is_ratio: bool = True,
):
    assert np.all(np.array(splits) > 0.)

    data_len = get_dict_len(args)

    if is_ratio:
        assert abs(float(np.array(splits).sum()) - 1.0) < 1e-8
    else:
        assert sum(splits) == data_len

    indice = np.arange(data_len)

    if do_shuffle:
        np.random.shuffle(indice)

    idx = 0
    splits_size = []
    for r in splits[:-1]:
        if is_ratio:
            idx += int(data_len * r)
        else:
            idx += r
        splits_size.append(idx)
    split_indice = np.split(indice, splits_size)

    split_args = []
    for _indice in split_indice:
        _split_args = {}

        for k1, v1 in args.items():
            if isinstance(v1, Dict):
                _split_args[k1] = {}
                for k2, v2 in v1.items():
                    _split_args[k1][k2] = v2[_indice]
            else:
                _split_args[k1] = v1[_indice]

        split_args.append(_split_args)

    return split_args


def dict_random_select(args: T, p: float):
    _l = get_dict_len(args)

    indice = []
    for idx in tqdm(range(_l)):
        _sp = random.random()
        if _sp > p:
            continue
        indice.append(idx)

    # all_indices = np.arange(_l)
    # mask = np.random.rand(_l) <= p
    # indice = all_indices[mask]

    #

    selected_args = {}
    for k1, v1 in args.items():
        if isinstance(v1, Dict):
            selected_args[k1] = {}
            for k2, v2 in v1.items():
                selected_args[k1][k2] = v2[indice]
        else:
            selected_args[k1] = v1[indice]

    return selected_args


# --- #


def get_noise_like(x: torch.Tensor, generator: torch.Generator = None):
    # normal distribution
    noise = torch.randn(
        x.shape,
        generator=generator,
        dtype=x.dtype,
        device=x.device,
    )
    return noise


def get_tensor_like(_in: torch.Tensor, _as: torch.Tensor, dim: int = -1):
    while len(_in.shape) < len(_as.shape):
        _in = _in.unsqueeze(dim=dim)
    return _in
