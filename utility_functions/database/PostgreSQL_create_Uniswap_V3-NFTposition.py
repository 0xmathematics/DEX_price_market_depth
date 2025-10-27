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
original_sql = """    
        CREATE TABLE IF NOT EXISTS Uniswap_LP_Position (
            id                SERIAL PRIMARY KEY,
            blockchain        varchar(20) NOT NULL, 
            project_name      varchar(20) NOT NULL, 
            token_id          BIGINT NOT NULL,
            address           varchar(42) NOT NULL,
            nonce             BIGINT NOT NULL,
            operator          varchar(42),
            token0            varchar(42) NOT NULL,
            token1            varchar(42) NOT NULL,
            fee               INTEGER NOT NULL,
            tick_lower        INTEGER NOT NULL,
            tick_upper        INTEGER NOT NULL,
            liquidity         NUMERIC NOT NULL,
            fee_growth_inside0_last_x128 NUMERIC ,
            fee_growth_inside1_last_x128 NUMERIC,
            tokens_owed0      NUMERIC,
            tokens_owed1      NUMERIC,
            last_updated      TIMESTAMPTZ DEFAULT now(),
            UNIQUE (blockchain, token_id)   -- combination unique

        );
        """
new_sql = """   
        CREATE EXTENSION IF NOT EXISTS citext;  --run once only for on database 
        CREATE TABLE IF NOT EXISTS Uniswap_LP_Position (
            id                SERIAL PRIMARY KEY,
            blockchain        CITEXT NOT NULL, 
            project_name      CITEXT NOT NULL, 
            token_id          BIGINT NOT NULL,
            address           CITEXT NOT NULL,
            nonce             BIGINT NOT NULL,
            operator          varchar(42),
            token0            CITEXT NOT NULL,
            token1            CITEXT NOT NULL,
            fee               INTEGER NOT NULL,
            tick_lower        INTEGER NOT NULL,
            tick_upper        INTEGER NOT NULL,
            liquidity         NUMERIC NOT NULL,
            fee_growth_inside0_last_x128 NUMERIC ,
            fee_growth_inside1_last_x128 NUMERIC,
            tokens_owed0      NUMERIC,
            tokens_owed1      NUMERIC,
            owner_address     CITEXT NOT NULL DEFAULT '0x666Ef6654B56885af2351c4C375519D7D8CC87a4',
            last_updated      TIMESTAMPTZ DEFAULT now(),
            check (char_length(address) = 42),
            check (char_length(token0) = 42),
            check (char_length(token1) = 42),
            check (char_length(owner_address) = 42),
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
    INSERT INTO Uniswap_LP_Position (
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
            ALTER TABLE Uniswap_LP_Position
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
cur.execute("DELETE FROM Uniswap_LP_Position where id = %s", (1,) )  # replace 'employees' with your table name
# delete row where id = 1, 2, 3 #
cur.execute("DELETE FROM Uniswap_LP_Position where id in %s", ((1,2,3),) )  # replace 'employees' with your table name
conn.commit()
# delete everything

cur = conn.cursor()
cur.execute("DELETE FROM Uniswap_LP_Position;")  # replace 'employees' with your table name
conn.commit()




# Run powershell as admin and restart services as follows
# Restart-Service -Name "postgresql-x64-17"
# or win+R services.msc postgresql-x64-17 restart








#%%
################################
# Delete table
################################
cur.execute("DROP TABLE IF EXISTS active_uniswap_v3_lp_mv CASCADE;") 

# Drop table if it exists #smart_contracts_abi_copy #
cur.execute("DROP TABLE IF EXISTS Uniswap_LP_Position CASCADE;")  # replace 'employees' with your table name
conn.commit()

# more fomal use

table_name = 'Uniswap_LP_Position'
sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
        sql.Identifier(table_name)
    )