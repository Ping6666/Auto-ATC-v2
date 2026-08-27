from typing import Dict, List

import numpy as np

from core.utils import Timer, mkdir, dump_json
from core.storage import OpenScope_DataStorage
from core.storage.utils import get_callsigns_info
from simulation.environment import Env

T = Dict[str, Dict[str, str | float | List | Dict]]


class Tape():
    storage: Dict[str, List]

    def __init__(self, save_folder: str):
        self.save_folder = save_folder

        self.keys = [
            'state',
            'action',
            'reward',
            'info',
            #
            'ils_info',
        ]
        self.storage = {}

        for k in self.keys:
            self.storage[k] = []
        return

    def push_next(self, args: Dict):
        for k in self.keys:
            arg = args.get(k)
            if arg is not None:
                self.storage[k].append(arg)
        return

    def save(self):
        f_folder = self.save_folder
        mkdir(f_folder, can_exists=True)

        for k in self.keys:
            obj = self.storage[k]
            ck_f_name = f"{f_folder}/{k}.json"
            dump_json(obj, ck_f_name)
        return


class Game():

    def __init__(
        self,
        env: Env,
        tape: Tape,
        ds: OpenScope_DataStorage,
        save_folder: str,
    ):
        self.env = env
        self.tape = tape
        self.ds = ds

        self.save_folder = save_folder

        self.c_info: T = {}

        self.reset_worker()
        return

    @property
    def terminal(self) -> bool:
        if self.done:
            return True
        return False

    def reset_worker(self):
        self.done = False

        self.t = Timer()
        self.times: List[Dict[str, float]] = []

        self.t_model = 0.
        self.t_save = 0.

        #

        _state = self.env.reset()

        args = {'state': _state, 'action': [], 'reward': 0, 'info': []}
        self.tape.push_next(args)

        self.ds.append(_state)

        #

        self.t.start()
        return

    def step_worker(
        self,
        parsed_commands: List[np.ndarray],
        callsigns_ils_info: List = [],
    ):
        if self.terminal:
            print("Game | The game has been terminated!")
            raise AssertionError

        #

        self.t.start()
        _state, _reward, _, info = self.env.step(actions=parsed_commands)
        self.t.end()
        t1 = self.t.get_time_spend()

        #

        self.t.start()
        args = {
            'state': _state,
            'action': parsed_commands,
            'reward': _reward,
            'info': info,
            'ils_info': callsigns_ils_info,
        }
        self.tape.push_next(args)
        self.t.end()
        t2 = self.t.get_time_spend()

        #

        self.t.start()
        self.ds.append(_state)
        self.t.end()
        t3 = self.t.get_time_spend()

        #

        self.t.start()
        _callsigns = self.ds.get_callsigns()
        for c in _callsigns:
            # for all callsigns curr. in the airspace
            if c not in self.c_info.keys():
                _rwy_name = self.ds.storage[c]['rwy_ori']
                self.c_info[c] = {
                    'rwy_ori': _rwy_name,
                    'can_ils': False,
                    'done_ils': False,
                    'len': 0,
                }

        all_callsigns = list(self.ds.storage.keys())
        _scanned_info = get_callsigns_info(info, all_callsigns)
        for c, _info in _scanned_info.items():
            if c in self.c_info.keys():
                for _i in _info:
                    self.c_info[c][_i] = True
        self.t.end()
        t4 = self.t.get_time_spend()

        #

        self.times.append({
            'model': self.t_model,
            'env.step': t1,
            'tape.push_next': t2,
            'data_storage._add': t3,
            'c_info': t4,
            'self.save': self.t_save,
        })

        self.t_model = 0.
        self.t_save = 0.

        #

        self.t.start()
        return

    def close_worker(self):
        print(f"\nGame | {self.env.uid} done, will close peacefully!")

        del self.env
        self.env = None
        self.done = True
        return

    def keep_time(self):
        self.t.end()
        self.t_model = self.t.get_time_spend()
        return

    def save(self, idx: int):
        folder = self.save_folder
        mkdir(folder, can_exists=True)
        game_folder = f"{folder}/game"
        mkdir(game_folder, can_exists=True)
        parsed_folder = f"{folder}/parsed"
        mkdir(parsed_folder, can_exists=True)
        samples_folder = f"{folder}/samples"
        mkdir(samples_folder, can_exists=True)

        self.t.start()

        #

        self.tape.save()

        fname = f"{game_folder}/spend_time.json"
        dump_json(self.times, fname)

        #

        for c in self.c_info.keys():
            _l = len(self.ds.storage[c]['time'])
            self.c_info[c]['len'] = _l

        fname = f'{parsed_folder}/callsigns_info-{idx:05d}.json'
        if idx == -1:
            fname = f'{parsed_folder}/#callsigns_info.json'
        dump_json(self.c_info, fname)

        if idx == -1:
            for c, v in self.c_info.items():
                _folder = f"{samples_folder}/{c}/raw"
                mkdir(_folder, can_exists=True)

                fname = f'{_folder}/info.json'
                dump_json(v, fname)

        #

        self.t.end()
        self.t_save = self.t.get_time_spend()
        return
