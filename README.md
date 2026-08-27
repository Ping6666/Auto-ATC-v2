# Generative Machine Learning for Air Traffic Control Decision Support: Trajectory Prediction and Command Generation

This repository focuses on trajectory prediction for one ego aircraft at a time. Given the ego aircraft's recent trajectory and surrounding airspace context, the model predicts a future trajectory for that aircraft. The code is intended for research reproduction and extension in terminal-area aircraft trajectory forecasting.

## Related Repositories

- [OpenSky-DL](https://github.com/Ping6666/OpenSky-DL): downloads ADS-B trajectory data from the OpenSky Network Trino database.
- [openscope-env](https://github.com/Ping6666/openscope-env): provides the OpenScope-based closed-loop interaction environment for the broader decision-support workflow.

## Repository Layout

```text
.
├── env/
│   ├── environment.yml          # Conda environment definition
│   ├── requirements.txt         # Python package requirements
│   └── README.md                # Environment setup notes
├── anws/
│   ├── data_preprocess.py       # Preprocess ANWS data
│   └── utils.py                 # ANWS preprocessing helpers
├── opensky/
│   ├── data_preprocess.py       # Preprocess OpenSky-DL output
│   └── utils.py                 # OpenSky preprocessing helpers
├── runs/
│   ├── README.md                # Published runs
│   ├── RCTP/single/             # Published RCTP run
│   └── RJTT/single/             # Published RJTT run
├── src/
│   ├── sampler.py               # Sample aircraft trajectory windows
│   ├── packer.py                # Pack samples into train/val/test datasets
│   ├── train.py                 # Distributed training entry point
│   ├── inference.py             # Checkpoint inference entry point
│   ├── interaction.py           # Closed-loop interaction entry point
│   ├── common/                  # Shared plotting and checkpoint helpers
│   ├── core/
│   │   ├── config.py            # Runtime configuration wrappers
│   │   ├── const.py             # Feature definitions and airport constants
│   │   ├── dataset/             # Packed dataset utilities
│   │   ├── diffuser/            # DDPM, DDIM, and flow-matching schedulers
│   │   ├── model/
│   │   │   └── single.py        # Supported single-aircraft trajectory model
│   │   ├── norm/                # Normalization modules
│   │   ├── pipeline/            # Training and inference pipelines
│   │   └── storage/             # ADS-B/OpenScope data loaders
│   ├── simulation/              # OpenScope interaction utilities
│   └── tools/
│       ├── data/                # Data visualization tools
│       ├── inference/           # Inference reports and plots
│       └── interaction/         # Closed-loop report tools
└── README.md
```

## Published Runs

The published [RJTT and RCTP runs](runs/README.md) each include checkpoints `20` through `200`, training and reconstruction records, trajectory-prediction error reports, closed-loop interaction reports, reproduction commands, selected results, and rendered closed-loop interaction video links.

## Environment Setup

Create the Conda environment and install the Python dependencies:

```bash
conda env create -f env/environment.yml
conda activate auto-atc-v2
uv pip install -r env/requirements.txt
```

## Reproduction Workflow

The commands below are reusable templates. For the exact published parameters, see the [RJTT](runs/RJTT/single/README.md#reproduction-commands) and [RCTP](runs/RCTP/single/README.md#reproduction-commands) runs.

### 1. Prepare Data

The published experiments use ADS-B trajectory data from two sources: OpenSky for RJTT and ANWS for RCTP.

For OpenSky data, use [OpenSky-DL](https://github.com/Ping6666/OpenSky-DL). The downloader should produce a folder with `flightlist.csv` and per-flight CSV files under `flights/csv/`.

Preprocess OpenSky-DL output with:

```bash
python ./opensky/data_preprocess.py \
  --data-folder /path/to/opensky_download/{airport}/{from_date}_{to_date}/
```

Preprocess ANWS data with:

```bash
python ./anws/data_preprocess.py \
  --data-folder /path/to/anws_adsb/ \
  --save-folder /path/to/preprocessed_adsb/
```

### 2. Sample Single-Aircraft Trajectories

```bash
python ./src/sampler.py \
  --data-folder /path/to/preprocessed_adsb/{airport}/{date-range}/ \
  --save-folder ./save/sampled/ \
  --mode single \
  --seed 12345 \
  --sampling-probability 1.0 \
  --idx-step 10 \
  --past-len 30 \
  --future-len 15 \
  --max-num-aircraft 40 \
  --icao {airport}
```

Use `--only-ifr` to sample only IFR flights.

### 3. Pack the Sampled Dataset

```bash
python ./src/packer.py \
  --sample-folder ./save/sampled/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/packed/ \
  --seed 12345 \
  --sampling-probability 0.5
```

The packer computes normalization statistics and writes packed train, validation, and test datasets.

### 4. Train the Model

```bash
OMP_NUM_THREADS=4 CUDA_VISIBLE_DEVICES=0 torchrun \
  --master_port=29510 \
  --nnodes=1 \
  --nproc_per_node=1 \
  ./src/train.py \
  --packed-folder ./save/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/train/ \
  --seed 12345 \
  --num-epochs 300 \
  --inf-per-num-epochs 20 \
  --save-ckpt-per-num-epochs 20 \
  --batch-size 180 \
  --inf-batch-size 1800 \
  --out-mode original \
  --diffuser ddim \
  --model-key-nargs L_04 x_on \
  --opt-key-nargs opt_1e-3 \
  --cold-inf
```

### 5. Run Inference

```bash
python ./src/inference.py \
  --ckpt-folder ./save/train/YYYY_MM_DD-HH_MM_SS/ \
  --packed-folder ./save/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/inference/ \
  --device cuda:0 \
  --seed 12345 \
  --batch-size 1800 \
  --inf-len 1024 \
  --num-pred 20 \
  --ckpt-idx-nargs 20 40 60
```

`--num-pred` controls how many stochastic trajectory predictions are generated for each input. Numeric checkpoint IDs are zero-padded internally, so `20` refers to `ckpt/000020.pt`.

The airport-specific checkpoint folders and selected checkpoint indices are listed with the [published runs](runs/README.md). A compatible packed dataset is still required because the runs intentionally omit packed data.

### 6. Plot Prediction Errors

```bash
python ./src/tools/inference/plot_error.py \
  --save-folder ./save/inference_report/ \
  --inf-folder-nargs ./save/inference/YYYY_MM_DD-HH_MM_SS/ \
  --ckpt-idx-nargs 20 40 60 \
  --num-pred 20
```

The report script writes summary statistics and box plots for prediction error over the forecast horizon.

### 7. Run Closed-Loop Interaction

Closed-loop interaction runs inside [openscope-env](https://github.com/Ping6666/openscope-env). The interaction code from this repository must be copied into `openscope-env` before building the production image, because `openscope-env/Dockerfile.prod` copies `./new-src` into the container as `/home/user/src`.

From the parent folder that contains both repositories, preserve any existing `new-src` directory before copying the Auto-ATC source:

```bash
cd /path/to/openscope-env
if [ -e ./new-src ]; then
  mv ./new-src "./new-src.backup-$(date +%Y%m%d-%H%M%S)"
fi
cp -r /path/to/Auto-ATC-v2/src/ ./new-src

bash ./build.sh prod

docker run -it --rm --shm-size 32G --gpus all \
  -v /path/to/save:/home/user/save \
  -v /path/to/Auto-ATC-v2:/home/user/Auto-ATC-v2:ro \
  openscope-env
```

Inside the container, start the OpenScope web server and Socket.IO relay:

```bash
bash /workspace/script/init_check.sh
```

Then run the interaction script with a trained checkpoint. The copied Auto-ATC code is under `/home/user/src`, and the mounted output folder is `/home/user/save`:

```bash
cd /home/user
python3 ./src/interaction.py \
  --num-proc 1 \
  --device cuda:0 \
  --seed 12345 \
  --batch-size 1800 \
  --ckpt-folder ./save/train/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/interaction/ \
  --save-step 500 \
  --num-exp 1 \
  --num-pred 20 \
  --ckpt-idx 20 \
  --nargs-take-idx 8 10 12 \
  --num-timestamps 5000
```

Use `--render` to run the OpenScope environment with rendering enabled. If you use a different host save folder in the `docker run -v` option, update the container paths passed to `--ckpt-folder` and `--save-folder` accordingly.

The selected long-run closed-loop interaction results use configuration `120/06` for RJTT runways `34L` and `34R`, and configuration `160/06` for RCTP runways `05L` and `23R`. Each configuration is labeled as `checkpoint/take_idx`. For reproduction commands, report details, and rendered videos, see the [RJTT](runs/RJTT/single/README.md) and [RCTP](runs/RCTP/single/README.md) runs.

---

*This README was drafted with AI assistance and reviewed by the authors.* (Created using Codex GPT-5.6 Sol with high reasoning.)
