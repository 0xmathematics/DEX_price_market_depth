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
#
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
path_utils = r'../'
path_utils ='/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions/database'

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
#conn.autocommit = True


cur = conn.cursor()

#%%
################################
# Query existing table
################################
# Query the data
cur.execute("SELECT * FROM uniswap_lp_state_info")
rows = cur.fetchall()
print("uniswap_pool_state_info:")
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


        );
        """
new_sql = """   
        CREATE EXTENSION IF NOT EXISTS citext;  --run once only for on database 
        CREATE TABLE IF NOT EXISTS uniswap_lp_state_info (
            id                  SERIAL PRIMARY KEY,
            blockchain          CITEXT NOT NULL, 
            project_name        CITEXT NOT NULL, 
            token_id            bigint NOT NULL,
            fee_growth_inside_current_0      NUMERIC NOT NULL,
            fee_growth_inside_current_1      NUMERIC NOT NULL,
            updated_at      TIMESTAMPTZ DEFAULT now(),
            UNIQUE (blockchain, project_name, token_id)   -- combination unique

        );
        """
cur.execute(new_sql)
        
conn.commit()
#%%
################################
# Insert the data
################################

# INSERT query
insert_query = """
    INSERT INTO uniswap_pool_state_info (
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
# Update Table
################################
# delete row where id = 1 # %s is a placeholder expect to receive a tuple format input
cur.execute('''
            ALTER TABLE uniswap_lp_state_info
            ADD COLUMN owner_address varchar(42) NOT NULL DEFAULT '0x666Ef6654B56885af2351c4C375519D7D8CC87a4';
            ''')  # replace 'employees' with your table name


conn.commit()
# delete everything

'''

# Run powershell as admin and restart services as follows
# Restart-Service -Name "postgresql-x64-17"
# or win+R services.msc postgresql-x64-17 restart
'''

#%%
################################
# Delete row
################################
# delete row where id = 1 # %s is a placeholder expect to receive a tuple format input
cur.execute("DELETE FROM uniswap_lp_state_info where id = %s", (1,) )  # replace 'employees' with your table name
# delete row where id = 1, 2, 3 #
cur.execute("DELETE FROM uniswap_lp_state_info where id in %s", ((1,2,3),) )  # replace 'employees' with your table name
conn.commit()
# delete everything

cur = conn.cursor()
cur.execute("DELETE FROM uniswap_lp_state_info;")  # replace 'employees' with your table name
conn.commit()




# Run powershell as admin and restart services as follows
# Restart-Service -Name "postgresql-x64-17"
# or win+R services.msc postgresql-x64-17 restart








#%%
################################
# Delete table
################################
cur.execute("DROP TABLE IF EXISTS uniswap_lp_state_info CASCADE;") 

# Drop table if it exists #smart_contracts_abi_copy #
cur.execute("DROP TABLE IF EXISTS Uniswap_LP_Position CASCADE;")  # replace 'employees' with your table name
conn.commit()

# more fomal use

table_name = 'Uniswap_LP_Position'
sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
        sql.Identifier(table_name)
    )