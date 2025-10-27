# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 00:14:15 2025

@author: Hang Miao
"""

import psycopg2
from datetime import datetime

# Connection settings
conn = psycopg2.connect(
    dbname="mydb",     # or 'mydb' if you created a new one
    user="postgres",
    password="tiancaimiaohang",  # 👈 Replace this
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        role TEXT,
        hired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

# Insert some data
cur.execute("""
    INSERT INTO employees (name, role) VALUES (%s, %s)
""", ("Bob", "Manager"))

# Query the data
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

print("Employees:")
for row in rows:
    print(row)

# Cleanup
conn.commit()
cur.close()
conn.close()




#%%
# delete table
# Connection settings
conn = psycopg2.connect(
    dbname="mydb",     # or 'mydb' if you created a new one
    user="postgres",
    password="tiancaimiaohang",  # 👈 Replace this
    host="localhost",
    port="5432"
)

cur = conn.cursor()


# Drop table if it exists
cur.execute("DROP TABLE IF EXISTS employees;")  # replace 'employees' with your table name

conn.commit()
cur.close()
conn.close()











