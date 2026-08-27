from typing import Dict, List
from argparse import ArgumentTypeError

from core.utils import get_time_str, get_torch_device


def custom_type(value):
    try:
        value = str(value).strip()

        if ":" in value:
            # 'start:stop:step'
            parts = value.split(":")

            if len(parts) != 3:
                raise ValueError("Expected format 'start:stop:step'.")

            start, stop, step = map(int, parts)

            _check1 = stop > start
            _check2 = step > 0
            if not _check1:
                raise ValueError("Expected {stop = } > {start = }")
            if not _check2:
                raise ValueError("Expected {step > 0}")

            _parsed = list(range(start, stop, step))
            if (stop - start) % step == 0:
                _parsed += [stop]

            return _parsed

        elif " " in value:
            # space-separated integers
            return list(map(int, value.split()))

        else:
            return [int(value)]

    except ValueError as e:
        raise ArgumentTypeError(f"Invalid value '{value}': {e}")


# --- #


class SampleConfig():

    def __init__(self, args):
        self.data_folder = args.data_folder
        self.save_folder = f"{args.save_folder}/{get_time_str()}"

        self.mode = args.mode

        self.seed = args.seed
        self.sampling_probability = args.sampling_probability

        self.icao = args.icao
        self.only_ifr = args.only_ifr

        self.idx_step = args.idx_step
        self.past_len = args.past_len
        self.future_len = args.future_len
        self.max_num_aircraft = args.max_num_aircraft
        return


class PackConfig():

    def __init__(self, args):
        self.sample_folder = args.sample_folder
        self.save_folder = f"{args.save_folder}/{get_time_str()}"

        self.seed = args.seed
        self.sampling_probability = args.sampling_probability
        return


class Config():

    model_key_nargs: List
    opt_key_nargs: List

    def __init__(self, args):
        self.packed_folder = args.packed_folder
        self.save_folder = f"{args.save_folder}/{get_time_str()}"

        if args.device:
            self.device = get_torch_device(args.device)

        self.seed = args.seed
        self.num_epochs = args.num_epochs
        self.inf_per_num_epochs = args.inf_per_num_epochs
        self.save_ckpt_per_num_epochs = args.save_ckpt_per_num_epochs

        self.batch_size = args.batch_size
        self.inf_batch_size = args.inf_batch_size

        self.out_mode = args.out_mode

        self.diffuser = args.diffuser
        self.model_key_nargs = args.model_key_nargs
        self.opt_key_nargs = args.opt_key_nargs

        self.cold_inf = args.cold_inf
        return


class InferenceConfig():

    ckpt_idx_list: List

    def __init__(self, args):
        self.ckpt_folder = args.ckpt_folder
        self.packed_folder = args.packed_folder
        self.save_folder = f"{args.save_folder}/{get_time_str()}"
        if args.device:
            self.device = get_torch_device(args.device)

        self.seed = args.seed

        self.batch_size = args.batch_size
        self.inf_len = args.inf_len
        self.num_pred = args.num_pred

        _ckpt_idx_list: List[int | str] = args.ckpt_idx_nargs

        self.ckpt_idx_list = []
        for ckpt_idx in _ckpt_idx_list:
            _ckpt_idx = ckpt_idx
            try:
                ckpt_idx = int(ckpt_idx)
                _ckpt_idx = f"{ckpt_idx:06}"
            except:
                pass
            self.ckpt_idx_list.append(_ckpt_idx)
        return


class InteractionConfig():

    seed: int
    nargs_ckpt_idx: List
    nargs_take_idx: List

    def __init__(self, args):
        self.num_proc = args.num_proc

        if args.device:
            self.device = get_torch_device(args.device)
        self.seed = args.seed
        self.batch_size = args.batch_size

        self.ckpt_folder = args.ckpt_folder
        self.save_folder = f"{args.save_folder}/{get_time_str()}"
        self.save_step = args.save_step

        self.num_exp = args.num_exp
        self.num_pred = args.num_pred
        self.nargs_ckpt_idx = args.ckpt_idx
        self.nargs_take_idx = args.nargs_take_idx

        self.assign_rwy = args.assign_rwy

        self.num_timestamps = args.num_timestamps
        self.render = args.render

        #

        assert self.batch_size % self.num_pred == 0
        assert self.num_timestamps % self.save_step == 0
        return
