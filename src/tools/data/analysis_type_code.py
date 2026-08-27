import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from copy import deepcopy
import time

from tqdm import tqdm
import requests

from core.icao24 import ICAO24_DICT
from core.utils import dump_json, load_json


def main():
    icao24_set = set()

    icao24_dict = deepcopy(ICAO24_DICT)
    icao24_dict_fname = f"./icao24_dict.json"

    # ref.:
    # 1. https://hexdb.io/
    # 2. https://www.flightradar24.com/data/aircraft/ja900a
    URL = 'https://hexdb.io/api/v1/aircraft'

    for _icao_hex in tqdm(icao24_set):
        if _icao_hex in icao24_dict:
            continue

        _url = f"{URL}/{_icao_hex}"

        r = requests.get(_url)
        _json = r.json()

        icao24_dict[_icao_hex] = _json
        dump_json(icao24_dict, icao24_dict_fname)

        # prevent abuse
        time.sleep(1)

    #

    dump_json(icao24_dict, icao24_dict_fname)

    print("DONE")
    return


"""
WARNING: Be cautious when using the API; do not take it for granted.

python ./src/tools/data/analysis_type_code.py
"""
if __name__ == '__main__':
    main()
