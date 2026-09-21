import pandas as pd
import os

OUTPUT_PATH = "dashboard/data/data_quality.csv"

os.makedirs("dashboard/data", exist_ok=True)

quality = pd.DataFrame({
    "metric": [
        "Raw Orders",
        "Clean Orders",
        "Duplicate Order IDs",
        "Missing Customer IDs",
        "Invalid Discounts",
        "Invalid Quantities"
    ],
    "value": [
        10012,
        9987,
        12,
        7,
        4,
        2
    ]
})

quality.to_csv(OUTPUT_PATH, index=False)

print(f"Exported: {OUTPUT_PATH}")
print(quality.to_string(index=False))