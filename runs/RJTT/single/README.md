# RJTT Single-Aircraft Run

This published Auto-ATC v2 run contains artifacts and results for single-aircraft trajectory prediction at RJTT / Japan Tokyo Haneda. See the repository README for shared [environment setup](../../../README.md#environment-setup) and the [reproduction workflow](../../../README.md#reproduction-workflow).

## Run Contents

```text
runs/RJTT/single/
├── train_save/2026_08_11-14_33_44/
│   ├── ckpt/000020.pt ... 000200.pt # checkpoints every 20 epochs
│   ├── record/*.json                # training and reconstruction records
│   └── #log.txt                     # training configuration and metadata
├── inf_report/2026_08_13-12_25_48/
│   └── stats_dict.json              # trajectory-prediction error statistics
└── int_report/
    ├── 2026_08_13-12_24_32/         # 34L/34R, 5,000-timestamp checkpoint sweep
    └── 2026_08_16-10_42_20/         # 34L/34R, 90,000-timestamp long-run interaction report
```

All ten checkpoints from `20` through `200` are included. The selected long-run closed-loop interaction results and rendered video cover runways `34L` and `34R` together and use configuration `120/06`, meaning checkpoint `120` with `take_idx=6`:

```text
train_save/2026_08_11-14_33_44/ckpt/000120.pt
```

## Run Configuration

| Category | Setting |
| --- | --- |
| ADS-B source | OpenSky |
| Data period | 2024-07-24 to 2024-07-31 |
| Closed-loop runways | `34L` and `34R` |
| Sampling | `mode=single`, `seed=12345`, `sampling_probability=1.0`, `only_ifr=false` |
| Trajectory window | `idx_step=10`, `past_len=30`, `future_len=15`, `max_num_aircraft=40` |
| Packing | `sampling_probability=0.5` |
| Training | 200 epochs, checkpoints every 20 epochs, 3 processes |
| Batches | `batch_size=1500`, `inf_batch_size=15000` |
| Model | DDIM, `out_mode=original`, `L_04 x_on`, `opt_1e-3`, cold inference |
| Dataset sizes | 2,308,087 training; 659,453 validation |

Use `runs/RJTT/single/train_save/2026_08_11-14_33_44/` as `--ckpt-folder`; the selected checkpoint index is `120`.

## Reproduction Commands

The commands below preserve the parameters used to produce the published RJTT results. Run the sampling, packing, training, and inference commands from the repository root. Replace source-data paths, generated timestamp folders, and CUDA device assignments for the local system. The sampled data, packed data, inference arrays, and raw interaction trajectories are not included in this run.

### Sampling and Packing

```bash
python ./src/sampler.py \
  --data-folder /path/to/preprocessed_adsb/RJTT/2024-07-24_2024-07-31/ \
  --save-folder ./save/rjtt-s/sampled/ \
  --mode single \
  --seed 12345 \
  --sampling-probability 1.0 \
  --idx-step 10 \
  --past-len 30 \
  --future-len 15 \
  --max-num-aircraft 40 \
  --icao RJTT

python ./src/packer.py \
  --sample-folder ./save/rjtt-s/sampled/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rjtt-s/packed/ \
  --seed 12345 \
  --sampling-probability 0.5
```

The published sampled and packed run IDs were `2026_08_07-16_47_13` and `2026_08_10-10_27_09`, respectively.

### Training

```bash
OMP_NUM_THREADS=4 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1,2 torchrun \
  --master_port=29510 \
  --nnodes=1 \
  --nproc_per_node=3 \
  ./src/train.py \
  --packed-folder ./save/rjtt-s/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rjtt-s/train_save/ \
  --seed 12345 \
  --num-epochs 200 \
  --inf-per-num-epochs 20 \
  --save-ckpt-per-num-epochs 20 \
  --batch-size 1500 \
  --inf-batch-size 15000 \
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
  --ckpt-folder ./runs/RJTT/single/train_save/2026_08_11-14_33_44/ \
  --packed-folder ./save/rjtt-s/packed/YYYY_MM_DD-HH_MM_SS/ \
  --save-folder ./save/rjtt-s/inf/ \
  --device cuda:0 \
  --seed 12345 \
  --batch-size 1500 \
  --inf-len 1024 \
  --num-pred 20 \
  --ckpt-idx-nargs 20 40 60 80 100 120 140 160 180 200

python ./src/tools/inference/plot_error.py \
  --save-folder ./save/rjtt-s/inf_report/ \
  --inf-folder-nargs ./save/rjtt-s/inf/YYYY_MM_DD-HH_MM_SS/ \
  --ckpt-idx-nargs 20 40 60 80 100 120 140 160 180 200 \
  --num-pred 20
```

### Selected Long-Run Closed-Loop Interaction

Run the following commands inside the OpenScope container described in the repository README. The repository must be mounted at `/home/user/Auto-ATC-v2`, as shown there. The RJTT environment operates runways `34L` and `34R` together, so no `--assign-rwy` argument is required. Two six-experiment batches produce the 12 runs summarized below; the two commands may use different available CUDA devices.

```bash
for device in cuda:0 cuda:1; do
  python3 ./src/interaction.py \
    --num-proc 3 \
    --device "$device" \
    --seed 12345 \
    --batch-size 1000 \
    --ckpt-folder /home/user/Auto-ATC-v2/runs/RJTT/single/train_save/2026_08_11-14_33_44/ \
    --save-folder ./save/rjtt-s/int/ \
    --save-step 10000 \
    --num-exp 6 \
    --num-pred 20 \
    --ckpt-idx 120 \
    --nargs-take-idx 6 \
    --num-timestamps 90000
done
```

Set the following variables to the two timestamped interaction directories created above, then generate the aggregate report. The published report used run IDs `2026_08_14-23_04_46` and `2026_08_14-23_04_54`.

```bash
RJTT_INT_RUN_A=./save/rjtt-s/int/YYYY_MM_DD-HH_MM_SS_A
RJTT_INT_RUN_B=./save/rjtt-s/int/YYYY_MM_DD-HH_MM_SS_B

python3 ./src/tools/interaction/report.py \
  --save-folder ./save/rjtt-s/int_report/ \
  --nargs-int-folder "$RJTT_INT_RUN_A" "$RJTT_INT_RUN_B" \
  --num-pred 20 \
  --ckpt-idx 120 \
  --nargs-take-idx 6 \
  --num-exp 6 \
  --save-step 10000 \
  --num-timestamps 90000

python3 ./src/tools/interaction/animate_traj.py \
  --folder "$RJTT_INT_RUN_A/000120/06/020-002" \
  --save-folder ./save/rjtt-s/int-ani/000120/06/020-002/ \
  --map \
  --icao RJTT
```

## Selected Results

The values below are the 90th-percentile trajectory-prediction errors for checkpoint `120` from `inf_report/2026_08_13-12_25_48/stats_dict.json`.

| Forecast step (10 s per step) | 3D distance error (NM) | y error (m) | x error (m) | Altitude error (ft) |
| --- | ---: | ---: | ---: | ---: |
| 0 | 1.382 | 1908.666 | 1720.875 | 256.491 |
| 5 | 1.434 | 2093.383 | 1678.223 | 535.917 |
| 10 | 2.281 | 2950.375 | 2657.441 | 942.818 |
| 14 | 3.328 | 4186.230 | 3837.091 | 1218.007 |

The combined `34L`/`34R` long-run closed-loop interaction metrics below come from configuration `120/06`'s `without_less` fields in `int_report/2026_08_16-10_42_20/score/game_score-90000.json`. These adjusted rates exclude unfinished aircraft whose recorded trajectories are shorter than 2,000 simulation timestamps; aircraft that landed, left the airspace, or were lost remain included. The values are aggregated over 12 runs.

| Configuration and metric | Min | Max | Mean | Median | Std |
| --- | ---: | ---: | ---: | ---: | ---: |
| `34L/34R — 120/06` adjusted ILS rate | 0.990 | 0.996 | 0.994 | 0.994 | 0.002 |
| `34L/34R — 120/06` adjusted landing rate | 0.935 | 0.984 | 0.959 | 0.957 | 0.013 |

## Rendered Closed-Loop Interaction Videos

- [Runways 34L and 34R closed-loop interaction video](https://www.youtube.com/watch?v=Hzbvv1qGais) — configuration `120/06`, experiment `020-002`.

---

*This README was drafted with AI assistance and reviewed by the authors.* (Created using Codex GPT-5.6 Sol with high reasoning.)
