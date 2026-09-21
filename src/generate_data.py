import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

# -----------------------------
# 1. Customers
# -----------------------------
num_customers = 500

regions = ["North", "South", "East", "West"]
segments = ["Enterprise", "SMB", "Consumer"]

customers = pd.DataFrame({
    "customer_id": range(1, num_customers + 1),
    "customer_name": [f"Customer_{i}" for i in range(1, num_customers + 1)],
    "region": np.random.choice(regions, num_customers),
    "segment": np.random.choice(segments, num_customers)
})

# -----------------------------
# 2. Products
# -----------------------------
num_products = 50

categories = ["Agriculture", "Food", "Industrial", "Consumer"]

products = pd.DataFrame({
    "product_id": range(1, num_products + 1),
    "product_name": [f"Product_{i}" for i in range(1, num_products + 1)],
    "category": np.random.choice(categories, num_products),
    "unit_price": np.round(np.random.uniform(50, 5000, num_products), 2)
})

# -----------------------------
# 3. Orders
# -----------------------------
num_orders = 10000

orders = pd.DataFrame({
    "order_id": range(1, num_orders + 1),
    "customer_id": np.random.randint(1, num_customers + 1, num_orders),
    "product_id": np.random.randint(1, num_products + 1, num_orders),
    "order_date": pd.date_range(
        start="2025-01-01",
        end="2026-08-31",
        periods=num_orders
    ),
    "quantity": np.random.randint(1, 101, num_orders),
    "discount": np.round(np.random.uniform(0, 0.30, num_orders), 2),
    "status": np.random.choice(
        ["Completed", "Pending", "Cancelled"],
        num_orders,
        p=[0.80, 0.15, 0.05]
    )
})

# -----------------------------
# 4. Add intentional data issues
# -----------------------------

# Missing customer IDs
orders.loc[10:16, "customer_id"] = np.nan

# Invalid discounts
orders.loc[20:23, "discount"] = 1.5

# Negative quantities
orders.loc[30:31, "quantity"] = -5

# Duplicate order records
duplicates = orders.iloc[100:112].copy()
orders = pd.concat([orders, duplicates], ignore_index=True)

# -----------------------------
# 5. Save datasets
# -----------------------------

customers.to_csv(OUTPUT_DIR / "customers.csv", index=False)
products.to_csv(OUTPUT_DIR / "products.csv", index=False)
orders.to_csv(OUTPUT_DIR / "orders_raw.csv", index=False)

print("Dataset generation complete.")
print(f"Customers: {len(customers)}")
print(f"Products: {len(products)}")
print(f"Orders: {len(orders)}")
print(f"Files saved to: {OUTPUT_DIR.resolve()}")