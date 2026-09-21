import sqlite3

DB_PATH = "data/business_analytics.db"

connection = sqlite3.connect(DB_PATH)

with open("sql/views.sql", "r") as file:
    sql_script = file.read()

connection.executescript(sql_script)
connection.commit()

print("SQL views created successfully.")

views = connection.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'view'
    ORDER BY name;
""").fetchall()

print("\nCreated views:")
for view in views:
    print("-", view[0])

connection.close()