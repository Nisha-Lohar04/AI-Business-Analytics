import sqlite3
import pandas as pd

DB_PATH = "data/business_analytics.db"

connection = sqlite3.connect(DB_PATH)

queries = {
    "Total Revenue": """
        SELECT ROUND(SUM(revenue), 2) AS total_revenue
        FROM orders
        WHERE status = 'Completed';
    """,

    "Total Orders": """
        SELECT COUNT(*) AS total_orders
        FROM orders
        WHERE status = 'Completed';
    """,

    "Revenue by Region": """
        SELECT
            c.region,
            ROUND(SUM(o.revenue), 2) AS revenue
        FROM orders o
        JOIN customers c
            ON o.customer_id = c.customer_id
        WHERE o.status = 'Completed'
        GROUP BY c.region
        ORDER BY revenue DESC;
    """,

    "Revenue by Category": """
        SELECT
            p.category,
            ROUND(SUM(o.revenue), 2) AS revenue
        FROM orders o
        JOIN products p
            ON o.product_id = p.product_id
        WHERE o.status = 'Completed'
        GROUP BY p.category
        ORDER BY revenue DESC;
    """,

    "Monthly Revenue": """
        SELECT
            strftime('%Y-%m', order_date) AS month,
            ROUND(SUM(revenue), 2) AS revenue
        FROM orders
        WHERE status = 'Completed'
        GROUP BY month
        ORDER BY month;
    """
}

print("\n========== BUSINESS ANALYTICS ==========\n")

for name, query in queries.items():
    print(f"\n--- {name} ---")
    result = pd.read_sql_query(query, connection)
    print(result.to_string(index=False))

connection.close()