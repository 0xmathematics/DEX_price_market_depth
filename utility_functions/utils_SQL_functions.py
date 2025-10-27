# -*- coding: utf-8 -*-
"""
Created on April 30 16:24:40 2025

@author: Hang
"""
import os
import requests
import json
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor
import sys
path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'

#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)

from dotenv import load_dotenv
env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)
db_pw = os.getenv('PostgreSQL_server_pw')  


    
#%%

import psycopg2
from datetime import datetime
import json
from tqdm import tqdm


# Autocommit mode is required to CREATE DATABASE
#conn.autocommit = True
def insert_uniswap_state_info(blockchain, project_name, address, tick, sqrt_price_x96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1,token_id):
    # Connection settings
    conn = psycopg2.connect(
        dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
        user="postgres",
        password= db_pw,  # 👈 Replace this
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    # INSERT pool state query
    insert_query_pool_state = """
        INSERT INTO uniswap_pool_state_info (
            blockchain, project_name, contract_address, tick, sqrt_price_x96
        ) VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT  (blockchain, project_name, contract_address)
        DO UPDATE SET
        tick = EXCLUDED.tick,
        sqrt_price_x96 = EXCLUDED.sqrt_price_x96,
        updated_at = now()
        RETURNING *;
    """
    pool_state_info_tuple = ( blockchain, project_name, address, tick, sqrt_price_x96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1)

    # INSERT LP state query
    insert_query_lp_state = """
        INSERT INTO uniswap_LP_state_info (
            blockchain, project_name, token_id,
            fee_growth_inside_current_0,fee_growth_inside_current_1
        ) VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT  (blockchain, project_name,token_id)
        DO UPDATE SET
        fee_growth_inside_current_0 = EXCLUDED.fee_growth_inside_current_0,
        fee_growth_inside_current_1 = EXCLUDED.fee_growth_inside_current_1,
        updated_at = now()
        RETURNING *;
    """
    LP_state_info_tuple = ( blockchain, project_name, token_id, feeGrowthInsideCurrent0,feeGrowthInsideCurrent1)

    try:
        cur.execute(
            insert_query_pool_state, 
            (
                blockchain,
                project_name,
                address,
                tick,
                sqrt_price_x96
           )        )
        conn.commit()
        new_row = cur.fetchone()
        print(new_row)
    
    except Exception as e:
        print("Error:", e)
        print(f"Failed to insert Pool State Info: {pool_state_info_tuple} \n")
        conn.rollback()  # 🔁 Reset the transaction
        
    try:
        cur.execute(
            insert_query_lp_state, 
            (
                blockchain,
                project_name,
                token_id,
                feeGrowthInsideCurrent0,
                feeGrowthInsideCurrent1
           )        )
        conn.commit()
        new_row = cur.fetchone()
        print(new_row)
    
    except Exception as e:
        print("Error:", e)
        print(f"Failed to insert LP State Info {LP_state_info_tuple} \n")
        conn.rollback()  # 🔁 Reset the transaction
    finally:
        cur.close()
        conn.close()
        
    return 

def insert_erc20(blockchain,symbol,name,address,decimals):
    # Connection settings
    conn = psycopg2.connect(
        dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
        user="postgres",
        password= db_pw,  # 👈 Replace this
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    # INSERT query
    insert_query = """
        INSERT INTO ERC20_Token (
            blockchain, symbol, name, address, decimals
        ) VALUES (%s, %s, %s, %s, %s)
        RETURNING *;
    """
    
    insert_data = {
        'blockchain': blockchain,
        'symbol': symbol,
        'name': name,
        'address': address,
        'decimals': decimals
    }
    try:
        cur.execute(
            insert_query, 
            (
                insert_data['blockchain'],
                insert_data['symbol'],
                insert_data['name'],
                insert_data['address'],
                insert_data['decimals']
           )        )
        conn.commit()
        new_row = cur.fetchone()
        print(new_row)
    
    except Exception as e:
        print("Error:", e)
        print(f"Failed to insert {insert_data}")
        conn.rollback()  # 🔁 Reset the transaction
    finally:
        cur.close()
        conn.close()
        
    return 

def insert_dex_info(blockchain, project_name, base, quote, fee, address, tick_spacing):
    # Connection settings
    conn = psycopg2.connect(
        dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
        user="postgres",
        password= db_pw,  # 👈 Replace this
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    # INSERT query
    insert_query = """
        INSERT INTO DEX_INFO (
            blockchain, project_name, base, quote, fee, address
        ) VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *;
    """
    dex_info_tuple = ( blockchain, project_name, base, quote, fee, address)
    print(dex_info_tuple)
    try:
        cur.execute(
            insert_query, 
            (
                blockchain,
                project_name,
                base,
                quote,
                fee, 
                address,
           )        )
        conn.commit()
        new_row = cur.fetchone()
        print(new_row)
    
    except Exception as e:
        print("Error:", e)
        print(f"Failed to insert {dex_info_tuple}")
        conn.rollback()  # 🔁 Reset the transaction
    finally:
        cur.close()
        conn.close()
        
    return 

def insert_uniswap_LP_info( blockchain, project_name, token_id, address,nonce,operator,\
 token0,token1, fee,tick_lower,tick_upper, liquidity, \
 fee_growth_inside0_last_x128, fee_growth_inside1_last_x128,\
  tokens_owed0, tokens_owed1, owner_address = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'):
    # Connection settings
    conn = psycopg2.connect(
        dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
        user="postgres",
        password= db_pw,  # 👈 Replace this
        host="localhost",
        port="5432"
    )

            

    cur = conn.cursor()
    # INSERT query
    insert_query = """
        INSERT INTO Uniswap_LP_Position (
            blockchain, project_name, token_id, address,nonce,operator,
             token0,token1, fee,tick_lower,tick_upper, liquidity, 
             fee_growth_inside0_last_x128, fee_growth_inside1_last_x128,
              tokens_owed0, tokens_owed1,owner_address
        ) VALUES (%s, %s, %s, %s,%s,%s, %s,%s, %s,%s,%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT  (blockchain, project_name, token_id)
        DO UPDATE SET
        last_updated = now()
        RETURNING *;
    """
    LP_info_tuple = (blockchain,  project_name, token_id,address,nonce,operator,\
     token0,token1, fee,tick_lower,tick_upper, liquidity, \
     fee_growth_inside0_last_x128, fee_growth_inside1_last_x128,\
      tokens_owed0, tokens_owed1)
    try:
        cur.execute(
            insert_query, 
            (
            blockchain, project_name, token_id,address,nonce,operator,\
             token0,token1, fee,tick_lower,tick_upper, liquidity, \
             fee_growth_inside0_last_x128, fee_growth_inside1_last_x128,\
              tokens_owed0, tokens_owed1,owner_address
           )        )
        conn.commit()
        new_row = cur.fetchone()
        print(new_row)
    
    except Exception as e:
        print("Error:", e)
        print(f"Failed to insert {LP_info_tuple}")
        conn.rollback()  # 🔁 Reset the transaction
    finally:
        cur.close()
        conn.close()
        
    return 

#insert_dex_info(**dex_info_dict)
def insert_uniswap_LP_df(df,blockchain, owner_address = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'):
    # df with format as follows:
    '''
	nonce	operator	token0	token1	fee	tick_lower	tick_upper	liquidity	fee_growth_inside0_last_x128	fee_growth_inside1_last_x128	tokens_owed0	tokens_owed1	token_id	project_name	address	blockchain
0	0	0x0000000000000000000000000000000000000000	0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599	0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2	500	256170	257610	0	115792089237316195423570985008687907853269984663954741150347495246215613984174	115792089237316195423570985008687907525089333380515952214974877058049970603509	0	0	241103	Uniswap_V3	0x4585FE77225b41b697C938B018E2Ac67Ac5a20c0	Ethereum
1	0	0x0000000000000000000000000000000000000000	0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599	0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2	3000	254580	260100	0	27408918582032824020308644762499	4066239123672047666767445551198136660746895	0	0	288012	Uniswap_V3	0xCBCdF9626bC03E24f779434178A73a0B4bad62eD	Ethereum
2	0	0x0000000000000000000000000000000000000000	0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599	0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2	500	254690	260230	0	25741596605375959039422652457332	3903476795211213273956810353968340895640524	0	0	295695	Uniswap_V3	0x4585FE77225b41b697C938B018E2Ac67Ac5a20c0	Ethereum

    '''
    df['blockchain']= blockchain
    df['owner_address']= owner_address
    tokens = df.to_dict(orient='records')
    for token in tqdm(tokens):
        
        print(token)
        insert_uniswap_LP_info(**token)
        
    return

def insert_erc20_df(df,blockchain):
    # df with format as follows:
    '''
    symbol           name  decimals                                     address
  0   USDC       USD Coin         6  0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85
  1   WETH  Wrapped Ether        18  0x4200000000000000000000000000000000000006
    '''
    df['blockchain']= blockchain
    tokens = df.to_dict(orient='records')
    for token in tokens:
        
        print(token)
        insert_erc20(**token)
        
    return 

def insert_dex_info_df(df,blockchain):
    # df with format as follows:
    '''
      project_name  base quote   fee                                     address
    0   Uniswap_V3  LINK  WETH  3000  0x19EA026886cbB7A900EcB2458636d72b5CaE223B
    '''
    df['blockchain']= blockchain
    tokens = df.to_dict(orient='records')
    for token in tokens:
        
        print(token)
        insert_dex_info(**token)
        
    return


def delete_entry(entry_id = 'all', sql_table = 'ERC20_Token'):
    # Connection settings
    conn = psycopg2.connect(
        dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
        user="postgres",
        password= db_pw,  
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    try:
        if entry_id == 'all':
            cur.execute(f"DELETE FROM {sql_table} returning *;")  # replace 'employees' with your table name
        else:
            cur.execute(f"DELETE FROM {sql_table} WHERE id ={entry_id} returning *;")  # replace 'employees' with your table name
        conn.commit()
        deleted_rows = cur.fetchall()
        for row in deleted_rows:
            print(row)
    
    except Exception as e:
        print("Error:", e)
        conn.rollback()  # 🔁 Reset the transaction
    finally:
        cur.close()
        conn.close()
        
    return 

#%%

