import pandas as pd

INPUT_FILE = "data/orders_raw.csv"
OUTPUT_FILE = "data/orders_clean.csv"

orders = pd.read_csv(INPUT_FILE)

# Remove duplicate orders
orders = orders.drop_duplicates(subset=["order_id"])

# Remove rows with missing customer IDs
orders = orders.dropna(subset=["customer_id"])

# Keep only valid discounts
orders = orders[
    (orders["discount"] >= 0) &
    (orders["discount"] <= 1)
]

# Keep only positive quantities
orders = orders[orders["quantity"] > 0]

# Convert IDs to integers
orders["customer_id"] = orders["customer_id"].astype(int)

# Convert date column
orders["order_date"] = pd.to_datetime(orders["order_date"])

# Calculate revenue
orders["revenue"] = (
    orders["quantity"]
    * orders["discount"].rsub(1)
)

# Save cleaned data
orders.to_csv(OUTPUT_FILE, index=False)

print("========== CLEANING COMPLETE ==========")
print(f"Clean rows: {len(orders)}")
print(f"Removed rows: {10012 - len(orders)}")
print(f"Saved to: {OUTPUT_FILE}")