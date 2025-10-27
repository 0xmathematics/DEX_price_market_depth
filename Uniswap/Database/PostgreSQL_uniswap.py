# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 00:14:15 2025

@author: Hang Miao
"""

import sys
path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)
from utils_functions import get_abi

# uniswap v3 deployment
# https://docs.uniswap.org/contracts/v3/reference/deployments

# Uniswap V3 NFT manager on ethereum
contract ='0xC36442b4a4522E871399CD717aBDD847Ab11FE88'
abi = get_abi(contract, blockchain = 'ethereum', abi_json = True)
#abi = get_abi_ethereum(contract, abi_json = True)
type(abi)


# WETH optimism
contract ='0x4200000000000000000000000000000000000006'
abi = get_abi(contract, 'optimism', abi_json = True)


# Uniswap V3 NFT manager on optimism
contract ='0xC36442b4a4522E871399CD717aBDD847Ab11FE88'
abi = get_abi(contract, 'optimism', abi_json = True)

# uniswap v3 USDC/WETH 
contract ='0xc1738D90E2E26C35784A0d3E3d8A9f795074bcA4'
abi = get_abi(contract, 'optimism', abi_json = True)

# uniswap v3 ETH/LINK failed
# optimism LINK-WETH
contract = "0x19EA026886cbB7A900EcB2458636d72b5CaE223B" 
abi = get_abi(contract, 'optimism', abi_json = True)

#%%


################################
# Create table to store ABI
################################
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Connection settings
conn = psycopg2.connect(
    dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
    user="postgres",
    password="tiancaimiaohang",  # 👈 Replace this
    host="localhost",
    port="5432"
)

# Autocommit mode is required to CREATE DATABASE
conn.autocommit = True


cur = conn.cursor()

# Create a table
cur.execute("""
        CREATE TABLE IF NOT EXISTS smart_contracts_abi_copy (
            id SERIAL PRIMARY KEY,
            blockchain varchar(20) NOT NULL,              -- e.g. Ethereum, BNB, Polygon
        	project_name varchar(20) NOT NULL,           -- Human-readable name
            contract_name text NOT NULL,           -- Human-readable name
            contract_address varchar(42) UNIQUE NOT NULL, -- Contract address (often checksum format)
            abi JSONB NOT NULL,                    -- The ABI stored as JSONB for querying
            created_at TIMESTAMPTZ DEFAULT now()
        );
        """)

# Insert some data

# INSERT query
insert_query = """
    INSERT INTO smart_contracts_abi_copy (
        blockchain, project_name, contract_name, contract_address, abi
    ) VALUES (%s, %s, %s, %s, %s)
    RETURNING id;
"""

insert_data = {
    'blockchain': 'Ethereum',
    'project_name': 'Uniswap-V3',
    'contract_name': 'Nonfungible_Position_Manager',
    'contract_address': '0xC36442b4a4522E871399CD717aBDD847Ab11FE88',
    'abi': abi
}

cur.execute(
    insert_query, (
        insert_data['blockchain'],
        insert_data['project_name'],
        insert_data['contract_name'],
        insert_data['contract_address'],
        insert_data['abi']
                   ))

# needed
conn.rollback()





#%%
# delete table
delete_query = """
DROP TABLE IF EXISTS smart_contracts_abi_copy CASCADE;
"""
cur.execute(delete_query)

# formal way
table_name = 'smart_contracts_abi_copy'
sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
        sql.Identifier(table_name)
    )
#%%
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
cur = conn.cursor()


# Drop table if it exists
cur.execute("DROP TABLE IF EXISTS employees;")  # replace 'employees' with your table name

conn.commit()
cur.close()
conn.close()











