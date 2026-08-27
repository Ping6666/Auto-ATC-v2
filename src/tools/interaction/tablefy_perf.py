import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

import numpy as np

from core.utils import load_json


def main():
    features = [
        "raw-total",
        "raw-land",
        "raw-less",
        "raw-land-avg_len",
        "with_less-land_rate",
        "without_less-land_rate",
        "without_less-can_ils_rate",
        "without_less-lost_rate",
        "without_less-leave_rate",
        "without_less-other_rate",
    ]

    fname = "/path/to/int_report/YYYY_MM_DD-HH_MM_SS/score/game_score-xxxxx.json"

    _json = load_json(fname)

    top_level_key = list(_json.keys())[0]
    _data = _json[top_level_key]

    print(f"{_data.keys() = }")

    # --- #

    header = f"{'Stat':<10}"
    for feat in features:
        header += f" | {feat}"
    print(header)
    print("-" * len(header))

    stats_rows = {"Min": [], "Max": [], "Mean": [], "Median": []}

    for feat in features:
        values = _data.get(feat, [])

        if not values:
            for key in stats_rows:
                stats_rows[key].append("N/A")
            continue

        stats_rows["Min"].append(round(min(values), 4))
        stats_rows["Max"].append(round(max(values), 4))
        stats_rows["Mean"].append(round(np.mean(values), 4))
        stats_rows["Median"].append(round(np.median(values), 4))

    for label, row_values in stats_rows.items():
        row_str = f"{label:<10}"
        for val in row_values:
            row_str += f" | {val:<15}"
        print(row_str)

    print("DONE")
    return


if __name__ == '__main__':
    main()
