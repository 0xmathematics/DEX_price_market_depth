# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 00:14:15 2025

@author: Hang Miao
"""

import numpy as np
import pandas as pd
import psycopg2
from datetime import datetime
import json
import os
import sys
path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'
#path_utils =/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions/database
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
path_utils = r'../'
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


cur = conn.cursor()
sql_query = '''
SELECT * FROM public."uniswap_LP_position"
LIMIT 100

'''
df = pd.read_sql(sql_query, conn)
print(df.head())


# Cleanup
conn.commit()
cur.close()
conn.close()



#%%
# Create a Pool state table
cur.execute("""
        CREATE TABLE IF NOT EXISTS uniswap_pool_state_info (
            id SERIAL PRIMARY KEY,
            blockchain varchar(20) NOT NULL,              -- e.g. Ethereum, BNB, Polygon
        	project_name varchar(20) NOT NULL,           -- Human-readable name
            contract_address varchar(42) NOT NULL,          -- Contract address (often checksum format)
            --state_price double precision NOT NULL,
            --state_price_inverse double precision NOT NULL,
            tick INTEGER NOT NULL,
            sqrt_price_X96 numeric NOT NULL,
            updated_at TIMESTAMPTZ DEFAULT now(),
            UNIQUE (blockchain, contract_address)   -- combination unique
        );
        """)

# Create a LP state table
cur.execute("""
        CREATE TABLE IF NOT EXISTS uniswap_LP_state_info (
            id SERIAL PRIMARY KEY,
            blockchain varchar(20) NOT NULL,              -- e.g. Ethereum, BNB, Polygon
        	project_name varchar(20) NOT NULL,           -- Human-readable name
            token_id BIGINT NOT NULL,
            fee_growth_inside_current_0 numeric NOT NULL,
            fee_growth_inside_current_1 numeric NOT NULL,
            updated_at TIMESTAMPTZ DEFAULT now(),
            UNIQUE (blockchain, project_name,token_id)   -- combination unique
        );
        """)        


conn.commit()

conn.rollback()



#%%
################################
# Delete table
################################


# Drop table if it exists #smart_contracts_abi_copy 
# 
cur.execute("DROP TABLE IF EXISTS uniswap_LP_state_info CASCADE;")  # replace 'employees' with your table name
conn.commit()
#%%
################################
# Update Table
################################
# rename
cur.execute('''
            ALTER TABLE uniswap_LP_state_info        
            RENAME COLUMN created_at TO updated_at;
            ''')  # replace 'employees' with your table name


conn.commit()

# rename
cur.execute('''
            ALTER TABLE uniswap_LP_state_info
            ADD COLUMN fee_growth_inside_current_0 numeric NOT NULL DEFAULT 0,
            ADD COLUMN fee_growth_inside_current_1 numeric NOT NULL DEFAULT 0;
            ''')  # replace 'employees' with your table name


conn.commit()



