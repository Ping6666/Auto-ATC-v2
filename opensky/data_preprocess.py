from argparse import ArgumentParser, Namespace

from utils import valid_flights, parse_flights


def get_args() -> Namespace:
    parser = ArgumentParser()

    # data
    parser.add_argument("--data-folder")

    args = parser.parse_args()
    return args


# --- #


def main(args):
    data_folder = args.data_folder

    valid_flights(data_folder)
    parse_flights(data_folder)

    print("DONE")
    return


"""
usage: data_preprocess.py [-h] [--data-folder DATA_FOLDER]

options:
  -h, --help            show this help message and exit
  --data-folder DATA_FOLDER


python ./opensky/data_preprocess.py --data-folder ./save/data-folder
"""
if __name__ == '__main__':
    args = get_args()
    main(args)
