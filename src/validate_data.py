import pandas as pd

ORDERS_FILE = "data/orders_raw.csv"

orders = pd.read_csv(ORDERS_FILE)

print("\n========== DATA QUALITY REPORT ==========\n")

# 1. Total rows
print(f"Total rows: {len(orders)}")

# 2. Duplicate orders
duplicates = orders["order_id"].duplicated().sum()
print(f"Duplicate order IDs: {duplicates}")

# 3. Missing customer IDs
missing_customers = orders["customer_id"].isna().sum()
print(f"Missing customer IDs: {missing_customers}")

# 4. Invalid discounts
invalid_discounts = ((orders["discount"] < 0) | (orders["discount"] > 1)).sum()
print(f"Invalid discounts: {invalid_discounts}")

# 5. Invalid quantities
invalid_quantities = (orders["quantity"] <= 0).sum()
print(f"Invalid quantities: {invalid_quantities}")

# 6. Missing values
print("\nMissing values:")
print(orders.isnull().sum())

print("\n========================================")