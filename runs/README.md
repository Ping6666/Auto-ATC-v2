# Published Runs

This directory contains the published Auto-ATC v2 runs for single-aircraft trajectory prediction and closed-loop interaction at two airports.

| Airport | ADS-B source | Data period | Selected checkpoint | Long-run configuration | Videos |
| --- | --- | --- | ---: | --- | --- |
| [RJTT / Japan Tokyo Haneda](RJTT/single/README.md) | OpenSky | 2024-07-24 to 2024-07-31 | `120` | `34L`, `34R`: `120/06` | [34L & 34R](https://www.youtube.com/watch?v=Hzbvv1qGais) |
| [RCTP / Taiwan Taoyuan](RCTP/single/README.md) | ANWS | 2025-07-23 to 2025-08-01 | `160` | `05L`, `23R`: `160/06` | [05L](https://www.youtube.com/watch?v=LdCgB3EPT9k), [23R](https://www.youtube.com/watch?v=TCjAKV_ZwSM) |

Each run contains:

```text
<airport>/single/
├── train_save/<run>/
│   ├── ckpt/*.pt          # checkpoints 20 through 200, every 20 epochs
│   ├── record/*.json      # training and reconstruction records
│   └── #log.txt           # training configuration and metadata
├── inf_report/<run>/      # trajectory-prediction error statistics and box plots
├── int_report/<run>/      # checkpoint sweeps and 90,000-timestamp reports
└── README.md              # configuration, commands, results, and video links
```

Closed-loop interaction configurations are labeled as `checkpoint/take_idx`. Each run's selected results and rendered closed-loop interaction videos use its selected checkpoint. All ten sweep checkpoints (`20`, `40`, ..., `200`) are included so the trajectory-prediction and closed-loop interaction sweeps can be inspected or rerun.

The raw source data, sampled arrays, packed datasets, inference arrays, and raw closed-loop interaction trajectories are intentionally not included.

---

*This README was drafted with AI assistance and reviewed by the authors.* (Created using Codex GPT-5.6 Sol with high reasoning.)
