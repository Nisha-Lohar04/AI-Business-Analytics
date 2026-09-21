import sqlite3

DB_PATH = "data/business_analytics.db"

connection = sqlite3.connect(DB_PATH)

with open("sql/top_products.sql", "r") as file:
    sql_script = file.read()

connection.executescript(sql_script)
connection.commit()

print("Top products view created successfully.")

connection.close()