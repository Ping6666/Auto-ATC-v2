from argparse import ArgumentParser, Namespace

from utils import valid_flights, parse_flights, ext_flights


def get_args() -> Namespace:
    parser = ArgumentParser()

    # data
    parser.add_argument("--data-folder", required=True)
    parser.add_argument("--save-folder", required=True)

    args = parser.parse_args()
    return args


# --- #


def main(args):
    data_folder = args.data_folder
    save_folder = args.save_folder

    valid_flights(data_folder, save_folder)
    parse_flights(data_folder, save_folder)
    ext_flights(save_folder)

    print("DONE")
    return


"""
usage: data_preprocess.py [-h] --data-folder DATA_FOLDER --save-folder SAVE_FOLDER

options:
  -h, --help            show this help message and exit
  --data-folder DATA_FOLDER
  --save-folder SAVE_FOLDER


python ./anws/data_preprocess.py --data-folder ./save/data-folder --save-folder ./save/save-folder
"""
if __name__ == '__main__':
    args = get_args()
    main(args)
