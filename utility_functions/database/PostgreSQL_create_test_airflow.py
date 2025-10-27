# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 00:14:15 2025

@author: Hang Miao
"""

import psycopg2
from datetime import datetime
import json
import os
import sys
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
path_utils = '/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)
from dotenv import load_dotenv
env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)
db_pw = os.getenv('PostgreSQL_server_pw')  


conn = psycopg2.connect(
    host="localhost",
    database="airflow_db",
    user="airflow_user",
    password="pw_airflow_psql"
)
# Autocommit mode is required to CREATE DATABASE
#conn.autocommit = True


cur = conn.cursor()

#%%
################################
# Query existing table
################################
# Query the data
cur.execute("SELECT * FROM ERC20_Token")
rows = cur.fetchall()
print("Contract_abi:")
for row in rows:
    print(row)

rows[0]

#%%
################################
# Create table 
################################

from psycopg2 import sql
from datetime import datetime


conn.rollback()

# Create a table
cur.execute("""
CREATE TABLE test_airflow_people (
    user_id int,
    username VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
        """)
        
conn.commit()
#%%
################################
# Insert the data
################################

# INSERT query
insert_query = """
    INSERT INTO ERC20_Token (
        blockchain, symbol, name, address, decimals
    ) VALUES (%s, %s, %s, %s, %s)
    RETURNING id;
"""

insert_data = {
    'blockchain': 'Ethereum',
    'symbol': 'WETHsss',
    'name': 'wrapped eth',
    'address': '0xC36442b4a4522E871399CD7s1aBDD847Ab11da88',
    'decimals': 18
}

cur.execute(
    insert_query, 
    (
        insert_data['blockchain'],
        insert_data['symbol'],
        insert_data['name'],
        insert_data['address'],
        insert_data['decimals']
   )        )

new_row = cur.fetchone()
print(new_row)

conn.rollback()
conn.commit()

cur.close()
# Close the connection
conn.close()
#%%
################################
# Delete row
################################
# delete row where id = 1 # %s is a placeholder expect to receive a tuple format input
cur.execute("DELETE FROM ERC20_Token where id = %s", (7,) )  # replace 'employees' with your table name
# delete row where id = 1, 2, 3 #
cur.execute("DELETE FROM ERC20_Token where id in %s", ((1,2,3),) )  # replace 'employees' with your table name
conn.commit()
# delete everything

cur = conn.cursor()
cur.execute("DELETE FROM ERC20_Token;")  # replace 'employees' with your table name
conn.commit()




# Run powershell as admin and restart services as follows
# Restart-Service -Name "postgresql-x64-17"
# or win+R services.msc postgresql-x64-17 restart








#%%
################################
# Delete table
################################


# Drop table if it exists #smart_contracts_abi_copy #
cur.execute("DROP TABLE IF EXISTS smart_contracts_abi CASCADE;")  # replace 'employees' with your table name
conn.commit()

# more fomal use

table_name = 'smart_contracts_abi_copy'
sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
        sql.Identifier(table_name)
    )