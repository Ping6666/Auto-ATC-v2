# RCTP Single-Aircraft Run

This published Auto-ATC v2 run contains artifacts and results for single-aircraft trajectory prediction at RCTP / Taiwan Taoyuan. See the repository README for shared [environment setup](../../../README.md#environment-setup) and the [reproduction workflow](../../../README.md#reproduction-workflow).

## Run Contents

```text
runs/RCTP/single/
├── train_save/2026_08_11-18_49_15/
│   ├── ckpt/000020.pt ... 000200.pt # checkpoints every 20 epochs
│   ├── record/*.json                # training and reconstruction records
│   └── #log.txt                     # training configuration and metadata
├── inf_report/2026_08_13-12_25_54/
│   └── stats_dict.json              # trajectory-prediction error statistics
└── int_report/
    ├── 2026_08_13-12_24_53/         # 05L, 5,000-timestamp checkpoint sweep
    ├── 2026_08_14-23_06_00/         # 23R, 5,000-timestamp checkpoint sweep
    ├── 2026_08_19-22_22_18/         # 05L, 90,000-timestamp long-run closed-loop interaction report
    └── 2026_08_18-17_06_17/         # 23R, 90,000-timestamp long-run closed-loop interaction report
```

All ten checkpoints from `20` through `200` are included. The selected long-run closed-loop interaction results and both rendered closed-loop interaction videos use configuration `160/06`, meaning checkpoint `160` with `take_idx=6`:

```text
train_save/2026_08_11-18_49_15/ckpt/000160.pt
```

## Run Configuration

| Category | Setting |
| --- | --- |
| ADS-B source | ANWS |
| Data period | 2025-07-23 to 2025-08-01 |
| Closed-loop runways | `05L` and `23R` |
| Sampling | `mode=single`, `seed=12345`, `sampling_probability=1.0`, `only_ifr=false` |
| Trajectory window | `idx_step=10`, `past_len=30`, `future_len=15`, `max_num_aircraft=30` |
| Packing | `sampling_probability=0.5` |
| Training | 200 epochs, checkpoints every 20 epochs, 3 processes |
| Batches | `batch_size=1800`, `inf_batch_size=18000` |
| Model | DDIM, `out_mode=original`, `L_04 x_on`, `opt_1e-3`, cold inference |
| Dataset sizes | 1,303,321 training; 372,377 validation |

Use `runs/RCTP/single/train_save/2026_08_11-18_49_15/` as `--ckpt-folder`; the selected checkpoint index is `160`.

## Reproduction Commands

The commands below preserve the parameters used to produce the published RCTP results. Run the sampling, packing, training, and inference commands from the repository root. Replace source-data paths, generated timestamp folders, and CUDA device assignments for the local system. The sampled data, packed data, inference arrays, and raw interaction trajectories are not included in this run.

### Sampling and Packing

```bash
python ./src/sampler.py \
  --data-folder /path/to/preprocessed_adsb/RCTP/2025-07-23_2025-08-01/ \
  --save-folder ./save/rctp-s/sampled/ \
  --mode single \
  --seed 12345 \
  --sampling-probability 1.0 \
  --idx-step 10 \
  --past-len 30 \
  --future-len 15 \
  --max-num-aircraft 30 \
  --icao RCTP

python ./src/packer.py \
  --sample-folder ./save/rctp-s/sampled/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rctp-s/packed/ \
  --seed 12345 \
  --sampling-probability 0.5
```

The published sampled and packed run IDs were `2026_08_07-16_47_18` and `2026_08_10-10_27_34`, respectively.

### Training

```bash
OMP_NUM_THREADS=4 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1,2 torchrun \
  --master_port=29520 \
  --nnodes=1 \
  --nproc_per_node=3 \
  ./src/train.py \
  --packed-folder ./save/rctp-s/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rctp-s/train_save/ \
  --seed 12345 \
  --num-epochs 200 \
  --inf-per-num-epochs 20 \
  --save-ckpt-per-num-epochs 20 \
  --batch-size 1800 \
  --inf-batch-size 18000 \
  --out-mode original \
  --diffuser ddim \
  --model-key-nargs L_04 x_on \
  --opt-key-nargs opt_1e-3 \
  --cold-inf
```

### Inference and Prediction-Error Report

The inference command below reuses the published checkpoints in this run and requires a compatible packed dataset.

```bash
python ./src/inference.py \
  --ckpt-folder ./runs/RCTP/single/train_save/2026_08_11-18_49_15/ \
  --packed-folder ./save/rctp-s/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rctp-s/inf/ \
  --device cuda:0 \
  --seed 12345 \
  --batch-size 1500 \
  --inf-len 1024 \
  --num-pred 20 \
  --ckpt-idx-nargs 20 40 60 80 100 120 140 160 180 200

python ./src/tools/inference/plot_error.py \
  --save-folder ./save/rctp-s/inf_report/ \
  --inf-folder-nargs ./save/rctp-s/inf/YYYY_MM_DD-HH_MM_SS/ \
  --ckpt-idx-nargs 20 40 60 80 100 120 140 160 180 200 \
  --num-pred 20
```

### Selected Long-Run Closed-Loop Interaction

Run the following commands inside the OpenScope container described in the repository README. The repository must be mounted at `/home/user/Auto-ATC-v2`, as shown there. For each runway, two six-experiment batches produce the 12 runs summarized below; the two commands may use different available CUDA devices.

```bash
for runway in 05L 23R; do
  for device in cuda:0 cuda:1; do
    python3 ./src/interaction.py \
      --num-proc 3 \
      --device "$device" \
      --seed 12345 \
      --batch-size 1000 \
      --ckpt-folder /home/user/Auto-ATC-v2/runs/RCTP/single/train_save/2026_08_11-18_49_15/ \
      --save-folder ./save/rctp-s/int/ \
      --save-step 10000 \
      --num-exp 6 \
      --num-pred 20 \
      --ckpt-idx 160 \
      --nargs-take-idx 6 \
      --num-timestamps 90000 \
      --assign-rwy "$runway"
  done
done
```

Set the following variables to the timestamped interaction directories created above, then generate one aggregate report per runway. The published 05L run IDs were `2026_08_16-10_45_04` and `2026_08_16-10_45_08`; the published 23R run IDs were `2026_08_16-10_48_25` and `2026_08_16-10_48_32`.

```bash
RCTP_05L_RUN_A=./save/rctp-s/int/YYYY_MM_DD-HH_MM_SS_A
RCTP_05L_RUN_B=./save/rctp-s/int/YYYY_MM_DD-HH_MM_SS_B
RCTP_23R_RUN_A=./save/rctp-s/int/YYYY_MM_DD-HH_MM_SS_C
RCTP_23R_RUN_B=./save/rctp-s/int/YYYY_MM_DD-HH_MM_SS_D

python3 ./src/tools/interaction/report.py \
  --save-folder ./save/rctp-s/int_report/ \
  --nargs-int-folder "$RCTP_05L_RUN_A" "$RCTP_05L_RUN_B" \
  --num-pred 20 \
  --ckpt-idx 160 \
  --nargs-take-idx 6 \
  --num-exp 6 \
  --save-step 10000 \
  --num-timestamps 90000

python3 ./src/tools/interaction/report.py \
  --save-folder ./save/rctp-s/int_report/ \
  --nargs-int-folder "$RCTP_23R_RUN_A" "$RCTP_23R_RUN_B" \
  --num-pred 20 \
  --ckpt-idx 160 \
  --nargs-take-idx 6 \
  --num-exp 6 \
  --save-step 10000 \
  --num-timestamps 90000

python3 ./src/tools/interaction/animate_traj.py \
  --folder "$RCTP_05L_RUN_A/000160/06/020-000" \
  --save-folder ./save/rctp-s/05L/int-ani/000160/06/020-000/ \
  --map \
  --icao RCTP

python3 ./src/tools/interaction/animate_traj.py \
  --folder "$RCTP_23R_RUN_A/000160/06/020-001" \
  --save-folder ./save/rctp-s/23R/int-ani/000160/06/020-001/ \
  --map \
  --icao RCTP
```

## Selected Results

The values below are the 90th-percentile trajectory-prediction errors for checkpoint `160` from `inf_report/2026_08_13-12_25_54/stats_dict.json`.

| Forecast step (10 s per step) | 3D distance error (NM) | y error (m) | x error (m) | Altitude error (ft) |
| --- | ---: | ---: | ---: | ---: |
| 0 | 0.811 | 1257.118 | 1094.099 | 113.778 |
| 5 | 1.090 | 1470.023 | 1471.241 | 498.966 |
| 10 | 2.000 | 2428.342 | 2418.805 | 916.833 |
| 14 | 3.000 | 3695.484 | 3571.645 | 1183.395 |

The long-run closed-loop interaction metrics below come from the `160/06` configuration's `without_less` fields in the two long-run closed-loop interaction reports' `score/game_score-90000.json` files. These adjusted rates exclude unfinished aircraft whose recorded trajectories are shorter than 2,000 simulation timestamps; aircraft that landed, left the airspace, or were lost remain included. The values are aggregated over 12 runs per runway.

| Configuration and metric | Min | Max | Mean | Median | Std |
| --- | ---: | ---: | ---: | ---: | ---: |
| `05L — 160/06` adjusted ILS rate | 0.978 | 0.995 | 0.988 | 0.988 | 0.005 |
| `05L — 160/06` adjusted landing rate | 0.900 | 0.938 | 0.918 | 0.916 | 0.010 |
| `23R — 160/06` adjusted ILS rate | 0.970 | 0.986 | 0.979 | 0.979 | 0.005 |
| `23R — 160/06` adjusted landing rate | 0.905 | 0.947 | 0.926 | 0.925 | 0.013 |

## Rendered Closed-Loop Interaction Videos

- [Runway 05L closed-loop interaction video](https://www.youtube.com/watch?v=LdCgB3EPT9k) — configuration `160/06`, experiment `020-000`.
- [Runway 23R closed-loop interaction video](https://www.youtube.com/watch?v=TCjAKV_ZwSM) — configuration `160/06`, experiment `020-001`.

---

*This README was drafted with AI assistance and reviewed by the authors.* (Created using Codex GPT-5.6 Sol with high reasoning.)
