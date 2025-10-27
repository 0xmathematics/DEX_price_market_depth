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
path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
path_utils = '/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)
from dotenv import load_dotenv
env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)
db_pw = os.getenv('PostgreSQL_server_pw')  

# Connection settings
conn = psycopg2.connect(
    dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
    user="postgres",
    password= db_pw,  # 👈 Replace this
    host="localhost",
    port="5432"
)

# Autocommit mode is required to CREATE DATABASE
conn.autocommit = True


cur = conn.cursor()

#%%
################################
# Query existing table
################################
# Query the data
cur.execute("SELECT * FROM DEX_INFO")
rows = cur.fetchall()
print("DEX_INFO:")
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

original_sql = """
        CREATE TABLE IF NOT EXISTS DEX_INFO (
            id SERIAL PRIMARY KEY,
            blockchain varchar(20) NOT NULL,              -- e.g. Ethereum, BNB, Polygon
            project_name varchar(20) NOT NULL,              -- e.g. Uniswap
            base varchar(20) NOT NULL,
            quote varchar(20)  NOT NULL,
            fee smallint NOT NULL,
            address varchar(42) NOT NULL, -- Contract address (often checksum format)
            created_at TIMESTAMPTZ DEFAULT now(),
            UNIQUE (blockchain, project_name, base, quote, fee)
        );
        """
new_sql = """
        CREATE EXTENSION IF NOT EXISTS citext;  --run once only for on database
        CREATE TABLE IF NOT EXISTS DEX_INFO (
            id SERIAL PRIMARY KEY,
            blockchain CITEXT NOT NULL,              -- e.g. Ethereum, BNB, Polygon
            project_name CITEXT NOT NULL,              -- e.g. Uniswap
            base CITEXT NOT NULL,
            quote CITEXT  NOT NULL,
            fee smallint NOT NULL,
            address CITEXT NOT NULL, -- Contract address (often checksum format)
            created_at TIMESTAMPTZ DEFAULT now(),
            check (char_length(address) = 42),
            UNIQUE (blockchain, project_name, base, quote, fee)
        );
        """


cur.execute(new_sql)

        
conn.commit()
#%%
################################
# Insert the data
################################
conn.rollback()

# INSERT query
insert_query = """
    INSERT INTO DEX_INFO (
        blockchain, project_name, base, quote, fee, address
    ) VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING *;
"""

insert_data = {
    'blockchain': 'Ethereum',
    'project_name': 'Uniswap_V3',
    'base': 'USDC',
    'quote': 'WETH',
    'fee': 3000,
    'address': '0xc1738D90E2E26C3578sA0d3E3d8A9f795074bcA4'
}

cur.execute(
    insert_query, 
    (
        insert_data['blockchain'],
        insert_data['project_name'],
        insert_data['base'],
        insert_data['quote'],
        insert_data['fee'],
        insert_data['address']
   )        )

new_row = cur.fetchone()
print(new_row)


conn.commit()

cur.close()
# Close the connection
conn.close()
#%%
################################
# Delete row
################################
# delete row where id = 1 # %s is a placeholder expect to receive a tuple format input
cur.execute("DELETE FROM DEX_INFO where id = %s", (1,) )  # replace 'employees' with your table name
# delete row where id = 1, 2, 3 #
cur.execute("DELETE FROM DEX_INFO where id in %s", ((1,2,3),) )  # replace 'employees' with your table name
conn.commit()
# delete everything

cur = conn.cursor()
cur.execute("DELETE FROM DEX_INFO;")  # replace 'employees' with your table name
conn.commit()




# Run powershell as admin and restart services as follows
# Restart-Service -Name "postgresql-x64-17"
# or win+R services.msc postgresql-x64-17 restart








#%%
################################
# Delete table
################################


# Drop table if it exists #smart_contracts_abi_copy #
cur.execute("DROP TABLE IF EXISTS DEX_INFO CASCADE;")  # replace 'employees' with your table name
conn.commit()

# more fomal use

table_name = 'DEX_INFO'
sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
        sql.Identifier(table_name)
    )