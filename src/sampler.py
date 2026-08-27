from argparse import ArgumentParser, Namespace

from core.utils import create_logger, set_torch_seeds, mkdir, dump_pkl, dump_npy
from core.config import SampleConfig
from core.storage import Opensky_DataStorage


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--data-folder", required=True)
    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--mode", required=True)

    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--sampling-probability", type=float, required=True)

    parser.add_argument("--icao", required=True)
    parser.add_argument('--only-ifr', action="store_true")

    parser.add_argument("--idx-step", type=int, required=True)
    parser.add_argument("--past-len", type=int, required=True)
    parser.add_argument("--future-len", type=int, required=True)
    parser.add_argument("--max-num-aircraft", type=int, required=True)

    args = parser.parse_args()
    return args


# --- #


def sample_single(cfg: SampleConfig):
    set_torch_seeds(cfg.seed)

    sp = cfg.sampling_probability
    s_kwargs = dict(
        max_num_aircraft=cfg.max_num_aircraft,
        idx_step=cfg.idx_step,
        past_len=cfg.past_len,
        future_len=cfg.future_len,
    )

    mkdir(cfg.save_folder)
    logger = create_logger(cfg.save_folder)
    logger.info(f"{vars(cfg) = }")

    #

    ds = Opensky_DataStorage(cfg.icao, cfg.only_ifr)
    ds.load(cfg.data_folder)
    logger.info(f"{len(ds.storage.keys()) = }")

    _start = ds.seg_tree.points[0]
    _end = ds.seg_tree.points[-1]
    logger.info("ds.seg_tree.points")
    logger.info(f"{_start} - {_end} = {_end - _start}")

    max_cs_len, _sample = ds.sampler_single(sp, s_kwargs)
    logger.info(f"{max_cs_len = } {cfg.max_num_aircraft = }")

    np_i, np_im, np_o, np_om, np_p, np_pm, np_f, np_fm = _sample

    dump_pkl(cfg, f"{cfg.save_folder}/#cfg.pkl")
    dump_npy(np_i, f"{cfg.save_folder}/i.npy")
    dump_npy(np_im, f"{cfg.save_folder}/im.npy")
    dump_npy(np_o, f"{cfg.save_folder}/o.npy")
    dump_npy(np_om, f"{cfg.save_folder}/om.npy")
    dump_npy(np_p, f"{cfg.save_folder}/p.npy")
    dump_npy(np_pm, f"{cfg.save_folder}/pm.npy")
    dump_npy(np_f, f"{cfg.save_folder}/f.npy")
    dump_npy(np_fm, f"{cfg.save_folder}/fm.npy")

    #

    for k in np_i.keys():
        logger.info(f"{k = } {np_i[k].shape = }")
    logger.info(f"{np_im.shape = }")
    logger.info(f"{np_o.shape = } {np_om.shape = }")
    logger.info(f"{np_p.shape = } {np_pm.shape = }")
    logger.info(f"{np_f.shape = } {np_fm.shape = }")

    for k in np_i.keys():
        logger.info(f"{k = } {np_i[k][0] = }")
    logger.info(f"{np_im[0] = }")
    logger.info(f"{np_o[0] = } {np_om[0] = }")
    logger.info(f"{np_p[0] = } {np_pm[0] = }")
    logger.info(f"{np_f[0] = } {np_fm[0] = }")

    logger.info("DONE")
    return


def sample_multiple(cfg: SampleConfig):
    set_torch_seeds(cfg.seed)

    sp = cfg.sampling_probability
    s_kwargs = dict(
        max_num_aircraft=cfg.max_num_aircraft,
        idx_step=cfg.idx_step,
        past_len=cfg.past_len,
        future_len=cfg.future_len,
    )

    mkdir(cfg.save_folder)
    logger = create_logger(cfg.save_folder)
    logger.info(f"{vars(cfg) = }")

    #

    ds = Opensky_DataStorage(cfg.icao, cfg.only_ifr)
    ds.load(cfg.data_folder)
    logger.info(f"{len(ds.storage.keys()) = }")

    _start = ds.seg_tree.points[0]
    _end = ds.seg_tree.points[-1]
    logger.info("ds.seg_tree.points")
    logger.info(f"{_start} - {_end} = {_end - _start}")

    max_cs_len, _sample = ds.sampler_multi(sp, s_kwargs)
    logger.info(f"{max_cs_len = } {cfg.max_num_aircraft = }")

    np_xyz, np_i, np_p, np_pm, np_f, np_fm = _sample

    dump_pkl(cfg, f"{cfg.save_folder}/#cfg.pkl")
    dump_npy(np_xyz, f"{cfg.save_folder}/xyz.npy")
    dump_npy(np_i, f"{cfg.save_folder}/i.npy")
    dump_npy(np_p, f"{cfg.save_folder}/p.npy")
    dump_npy(np_pm, f"{cfg.save_folder}/pm.npy")
    dump_npy(np_f, f"{cfg.save_folder}/f.npy")
    dump_npy(np_fm, f"{cfg.save_folder}/fm.npy")

    #

    logger.info(f"{np_xyz.shape = }")
    for k in np_i.keys():
        logger.info(f"{k = } {np_i[k].shape = }")
    logger.info(f"{np_p.shape = } {np_pm.shape = }")
    logger.info(f"{np_f.shape = } {np_fm.shape = }")

    logger.info(f"{np_xyz[0] = }")
    for k in np_i.keys():
        logger.info(f"{k = } {np_i[k][0] = }")
    logger.info(f"{np_p[0] = } {np_pm[0] = }")
    logger.info(f"{np_f[0] = } {np_fm[0] = }")

    logger.info("DONE")
    return


def main(cfg: SampleConfig):
    if cfg.mode == 'single':
        sample_single(cfg)
    elif cfg.mode == 'multiple':
        sample_multiple(cfg)
    else:
        raise AssertionError
    return


"""
usage: sampler.py [-h] --data-folder DATA_FOLDER --save-folder SAVE_FOLDER --mode MODE --seed SEED --sampling-probability SAMPLING_PROBABILITY [--only-ifr] --idx-step IDX_STEP --past-len PAST_LEN --future-len FUTURE_LEN --max-num-aircraft MAX_NUM_AIRCRAFT

options:
  -h, --help            show this help message and exit
  --data-folder DATA_FOLDER
  --save-folder SAVE_FOLDER
  --mode MODE
  --seed SEED
  --sampling-probability SAMPLING_PROBABILITY
  --only-ifr
  --idx-step IDX_STEP
  --past-len PAST_LEN
  --future-len FUTURE_LEN
  --max-num-aircraft MAX_NUM_AIRCRAFT
"""
if __name__ == '__main__':
    args = get_args()
    cfg = SampleConfig(args)
    main(cfg)
