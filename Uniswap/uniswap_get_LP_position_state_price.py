# -*- coding: utf-8 -*-
"""
Created on May 17 16:24:40 2025

@author: Hang
"""


import sys
#path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
# /home/hang/Documents/GitHub/DEX_Development_Kit/Uniswap
path_utils = r'../utility_functions'
path_utils = '/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)
uniswap_path = r'/home/hang/Documents/GitHub/DEX_Development_Kit/Uniswap'
sys.path.append(uniswap_path)

from utils_functions import get_abi
from dotenv import load_dotenv
from privateKey import *

env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)
import re
from collections import defaultdict
import os
from web3 import Web3
import numpy as np
import pandas as pd
import json
import psycopg2
import datetime
import time
#import tqdm
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor
from getpass import getpass
from utils_SQL_functions import insert_uniswap_state_info

# set the wd to the folder
#os.chdir(r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\Uniswap')
#os.chdir('/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/Uniswap')

#os.chdir('/home/hang/Documents/GitHub/DEX_Development_Kit/Uniswap')
#print("Current working directory:", os.getcwd())
from class_uniswap import Uniswap_v3
from multicall import Call, Multicall
import nest_asyncio
nest_asyncio.apply()

rpc_dict = {
    'Ethereum':os.getenv('infura_url_ethereum'),
    'Arbitrum' : os.getenv('infura_url_arbitrum') , 
    'Polygon' : os.getenv('infura_url_polygon'), 
    'Base' : os.getenv('infura_url_base'), 
    'Linea' : os.getenv('infura_url_linea') ,
    'Optimism' : os.getenv('infura_url_optimism') ,
    'Unichain' : os.getenv('infura_url_unichain') ,
    
    }
db_pw = os.getenv('PostgreSQL_server_pw')  

# Connection settings
conn = psycopg2.connect(
    dbname="crypto",     # default 'postgres' or 'xxx' if you created a new one
    user="postgres",
    password= db_pw,  # 👈 Replace this
    host="localhost",
    port="5432"
)


'''
# get block number/ timestamp/ datetime
block_number_current = web3.eth.block_number
block = web3.eth.get_block(block_number_current)
block_timestamp = block.timestamp
block_datetime = datetime.datetime.utcfromtimestamp(block_timestamp)
block_datetime.strftime("%Y-%m-%d %H:%M:%S")
'''
####################################
# Uniswap V3 get current state info
####################################


def uniswap_v3_state_info(contract_address, rpc_url, tick_lower, tick_upper, blocknumber = 'latest', ):
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"Collect","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"CollectProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid1","type":"uint256"}],"name":"Flash","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"observationCardinalityNextOld","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"observationCardinalityNextNew","type":"uint16"}],"name":"IncreaseObservationCardinalityNext","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Initialize","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0New","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],"name":"SetFeeProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"int256","name":"amount0","type":"int256"},{"indexed":false,"internalType":"int256","name":"amount1","type":"int256"},{"indexed":false,"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Swap","type":"event"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collect","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collectProtocol","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal0X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal1X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"flash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"}],"name":"increaseObservationCardinalityNext","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidity","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLiquidityPerTick","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"observations","outputs":[{"internalType":"uint32","name":"blockTimestamp","type":"uint32"},{"internalType":"int56","name":"tickCumulative","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityCumulativeX128","type":"uint160"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32[]","name":"secondsAgos","type":"uint32[]"}],"name":"observe","outputs":[{"internalType":"int56[]","name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]","name":"secondsPerLiquidityCumulativeX128s","type":"uint160[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"positions","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128","name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFees","outputs":[{"internalType":"uint128","name":"token0","type":"uint128"},{"internalType":"uint128","name":"token1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"feeProtocol0","type":"uint8"},{"internalType":"uint8","name":"feeProtocol1","type":"uint8"}],"name":"setFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"slot0","outputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint16","name":"observationIndex","type":"uint16"},{"internalType":"uint16","name":"observationCardinality","type":"uint16"},{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"},{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"bool","name":"unlocked","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],"name":"snapshotCumulativesInside","outputs":[{"internalType":"int56","name":"tickCumulativeInside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityInsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsInside","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool","name":"zeroForOne","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int16","name":"","type":"int16"}],"name":"tickBitmap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"","type":"int24"}],"name":"ticks","outputs":[{"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128","name":"liquidityNet","type":"int128"},{"internalType":"uint256","name":"feeGrowthOutside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"},{"internalType":"int56","name":"tickCumulativeOutside","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityOutsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsOutside","type":"uint32"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
    address = Web3.to_checksum_address(contract_address)
    contract = web3.eth.contract(address = address, abi = abi )
    slot_0 = contract.functions.slot0().call(block_identifier=blocknumber)
    tick_current = slot_0[1]
    sqrtPriceX96 = slot_0[0]
    feeGrowthGlobal0 = contract.functions.feeGrowthGlobal0X128().call(block_identifier=blocknumber)
    feeGrowthGlobal1 = contract.functions.feeGrowthGlobal1X128().call(block_identifier=blocknumber)
    
    feeGrowthOutside_lower = contract.functions.ticks(tick_lower).call(block_identifier=blocknumber)
    feeGrowthOutside0_lower = feeGrowthOutside_lower[2]
    feeGrowthOutside1_lower = feeGrowthOutside_lower[3]
    feeGrowthOutside_upper = contract.functions.ticks(tick_upper).call(block_identifier=blocknumber)
    feeGrowthOutside0_upper = feeGrowthOutside_upper[2]
    feeGrowthOutside1_upper = feeGrowthOutside_upper[3]
    
    feeBelowLower0 = feeGrowthOutside0_lower if (tick_current >= tick_lower) \
        else (feeGrowthGlobal0 - feeGrowthOutside0_lower)
    feeBelowLower1 = feeGrowthOutside1_lower if (tick_current >= tick_lower) \
        else (feeGrowthGlobal1 - feeGrowthOutside1_lower)
    feeAboveUpper0 = (feeGrowthGlobal0 - feeGrowthOutside0_upper) if (tick_current >= tick_upper) \
        else feeGrowthOutside0_upper
    feeAboveUpper1 = (feeGrowthGlobal1 - feeGrowthOutside1_upper) if (tick_current >= tick_upper) \
        else feeGrowthOutside1_upper
    
    feeGrowthInsideCurrent0 = feeGrowthGlobal0 - feeBelowLower0 - feeAboveUpper0
    feeGrowthInsideCurrent1 = feeGrowthGlobal1 - feeBelowLower1 - feeAboveUpper1
    '''
    f_o0_l = feeGrowthOutside_lower[2]
    f_o1_l = feeGrowthOutside_lower[3]
    f_o0_u = feeGrowthOutside_upper[2]
    f_o1_u = feeGrowthOutside_upper[3]
    '''
    return tick_current, sqrtPriceX96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1


def uniswap_v3_state_info_multicall(tick_current, sqrtPriceX96, feeGrowthGlobal0, feeGrowthGlobal1,\
                                    feeGrowthOutside0_lower, feeGrowthOutside1_lower, \
                                        feeGrowthOutside0_upper, feeGrowthOutside1_upper, ):


    
    feeBelowLower0 = feeGrowthOutside0_lower if (tick_current >= tick_lower) \
        else (feeGrowthGlobal0 - feeGrowthOutside0_lower)
    feeBelowLower1 = feeGrowthOutside1_lower if (tick_current >= tick_lower) \
        else (feeGrowthGlobal1 - feeGrowthOutside1_lower)
    feeAboveUpper0 = (feeGrowthGlobal0 - feeGrowthOutside0_upper) if (tick_current >= tick_upper) \
        else feeGrowthOutside0_upper
    feeAboveUpper1 = (feeGrowthGlobal1 - feeGrowthOutside1_upper) if (tick_current >= tick_upper) \
        else feeGrowthOutside1_upper
    
    feeGrowthInsideCurrent0 = feeGrowthGlobal0 - feeBelowLower0 - feeAboveUpper0
    feeGrowthInsideCurrent1 = feeGrowthGlobal1 - feeBelowLower1 - feeAboveUpper1
    '''
    f_o0_l = feeGrowthOutside_lower[2]
    f_o1_l = feeGrowthOutside_lower[3]
    f_o0_u = feeGrowthOutside_upper[2]
    f_o1_u = feeGrowthOutside_upper[3]
    '''
    return tick_current, sqrtPriceX96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1


def extract_fee_growth(sub_df, ticks_map):
    # Helper functions
    def get_fee(address, tick, index):
        try:
            return ticks_map[address][tick][index]
        except KeyError:
            print('error')
            return None

    sub_df['feeGrowthOutside0_lower'] = [
        get_fee(row['address'], row['tick_lower'], 2) for _, row in sub_df.iterrows()
    ]

    sub_df['feeGrowthOutside1_lower'] = [
        get_fee(row['address'], row['tick_lower'], 3) for _, row in sub_df.iterrows()
    ]

    sub_df['feeGrowthOutside0_upper'] = [
        get_fee(row['address'], row['tick_upper'], 2) for _, row in sub_df.iterrows()
    ]

    sub_df['feeGrowthOutside1_upper'] = [
        get_fee(row['address'], row['tick_upper'], 3) for _, row in sub_df.iterrows()
    ]

    return sub_df    

    


#%%
##########################
## Get active LP position
##########################
sql_query = '''
SELECT * FROM public."uniswap_lp_position"
--LIMIT 5
'''


df = pd.read_sql(sql_query, conn)
print(df.head())
#row_num=2
filter_1 = df['liquidity']>0
filter_2 = df['project_name'] =='Uniswap_V3'
df = df[ filter_1 & filter_2]
df['address'] = df['address'].apply(Web3.to_checksum_address)

unique_combinations = df[['blockchain', 'address']].drop_duplicates()
unique_combinations_nft = df[['blockchain', 'address','tick_lower','tick_upper','token_id']].drop_duplicates()



#%%

df_data=pd.DataFrame()

for blockchain, sub_df in unique_combinations_nft.groupby('blockchain'):
    print(f"Blockchain: {blockchain}")
    print(sub_df)
    web3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))
    calls = []
    for address, sub_sub_df in sub_df.groupby('address'):
        print(address)
        print(sub_sub_df)
        # get pool info
        

        calls.extend([
            Call(address, ['slot0()((uint160,int24,uint16,uint16,uint16,uint8,bool))',],  [[f'{address}.slot0', None]]), 
            Call(address, ['feeGrowthGlobal0X128()(uint256)'], [[f'{address}.feeGrowthGlobal0X128', None]]),
            Call(address, ['feeGrowthGlobal1X128()(uint256)'], [[f'{address}.feeGrowthGlobal1X128', None]])
        ])
        for row_num in range(len(sub_sub_df)):
            tick_lower = int(sub_sub_df.iloc[row_num]['tick_lower'])
            tick_upper = int(sub_sub_df.iloc[row_num]['tick_upper'])

            calls.extend([
                Call(address, ['ticks(int24)((uint128,int128,uint256,uint256,int56,uint160,uint32,bool))',tick_lower],  [[f'{address}.tick_lower.{tick_lower}', None]]), 
                Call(address, ['ticks(int24)((uint128,int128,uint256,uint256,int56,uint160,uint32,bool))',tick_upper],  [[f'{address}.tick_upper.{tick_upper}', None]])
            ])            
    
    multi = Multicall(calls, _w3=web3)
    results_pool_state_info = multi()

    
    # convert the multicall result to df
    structured_data = {}
    ticks_map = defaultdict(dict)
    for key, value in results_pool_state_info.items():
        address, field = key.split('.', 1)
        if address not in structured_data:
            structured_data[address] = {}
        
        if field == 'slot0':
            structured_data[address]['sqrtPriceX96'] = value[0]
            structured_data[address]['tick'] = value[1]
            #structured_data[address]['observationIndex'] = value[2]
            #structured_data[address]['observationCardinality'] = value[3]
            #structured_data[address]['observationCardinalityNext'] = value[4]
            #structured_data[address]['feeProtocol'] = value[5]
            #structured_data[address]['unlocked'] = value[6]
        elif field.startswith('tick'):
            
            tick_idx = int(field.split('.', 2)[1])
            if tick_idx not in ticks_map:
                
                ticks_map[address][tick_idx] = value

        else:
            structured_data[address][field] = value
    
        # Step 2: Combine into rows

    new_sub_df = extract_fee_growth(sub_df, ticks_map)
        # Step 3: Make DataFrame
        #df = pd.DataFrame(rows)
        
        #print(df.head())    
    
    
    

    
    
    
    
    # Convert to DataFrame
    df_pool_info = pd.DataFrame.from_dict(structured_data, orient='index')
    '''
    # Optional: Reorder columns
    desired_order = [
        'sqrtPriceX96', 'tick', 'observationIndex', 'observationCardinality', 
        'observationCardinalityNext', 'feeProtocol', 'unlocked',
        'feeGrowthGlobal0X128', 'feeGrowthGlobal1X128'
    ]
    df_pool_info = df_pool_info[desired_order]
    '''
    df_pool_info = df_pool_info.reset_index().rename(columns={'index': 'address'})
    
    
    merged_df = pd.merge(new_sub_df, df_pool_info, how='left', left_on='address', right_on='address')
    
    df_data = pd.concat([df_data,merged_df],ignore_index=True)
    
df_data['project_name'] ='Uniswap_V3'
    #%%

for row_num in range(len(df_data)):
    row = df_data.iloc[row_num]
    project_name = row['project_name']
    address = row['address']
    token_id = int(row['token_id'])
    blockchain = row['blockchain']
    tick_lower = int(row['tick_lower'])
    tick_upper = int(row['tick_upper'])
    tick_current = int(row['tick'])
    sqrtPriceX96 =  row['sqrtPriceX96']
    feeGrowthGlobal0 =  row['feeGrowthGlobal0X128']
    feeGrowthGlobal1 =  row['feeGrowthGlobal1X128']
    feeGrowthOutside0_lower =  row['feeGrowthOutside0_lower']
    feeGrowthOutside1_lower =  row['feeGrowthOutside1_lower']
    feeGrowthOutside0_upper =  row['feeGrowthOutside0_upper']
    feeGrowthOutside1_upper =  row['feeGrowthOutside1_upper']
    if project_name == 'Uniswap_V3':
        
        tick, sqrtPriceX96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1 = \
        uniswap_v3_state_info_multicall(tick_current, sqrtPriceX96, feeGrowthGlobal0, feeGrowthGlobal1,\
                                            feeGrowthOutside0_lower, feeGrowthOutside1_lower, \
                                                feeGrowthOutside0_upper, feeGrowthOutside1_upper, )
        insert_uniswap_state_info(blockchain, project_name, address, tick, sqrtPriceX96, feeGrowthInsideCurrent0, feeGrowthInsideCurrent1, token_id)
        


df_data.columns
type( df_data['feeGrowthGlobal0X128'][0] )
    #%%
    
# update  token information and DEX information from active LP related to Uniswap V3
    
    
    
sql_query = '''
SELECT * FROM public."uniswap_lp_position"
--LIMIT 5
'''


df = pd.read_sql(sql_query, conn)
print(df.head())
#row_num=2
filter_1 = df['liquidity']>0
filter_2 = df['project_name'] =='Uniswap_V3'
df = df[ filter_1 & filter_2]
df['address'] = df['address'].apply(Web3.to_checksum_address)

unique_combinations_address = df[['blockchain', 'address']].drop_duplicates()
unique_combinations_nft = df[['blockchain', 'address','tick_lower','tick_upper','token_id']].drop_duplicates()
    
    
from utils_SQL_functions import insert_erc20_df, delete_entry,\
    insert_dex_info_df    
    
for blockchain, sub_df in unique_combinations_address.groupby('blockchain'):
    
    

    web3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))
    print(web3.is_connected() )

    for row_num in range(len(sub_df)):
        row = df_data.iloc[row_num]
        contract_address = row['address']
        # construct uniswap v3 object
        uniswap_v3_obj = Uniswap_v3(contract_address, rpc_dict[blockchain])
        # ERC20 info
        df_coins_info = uniswap_v3_obj.coins_info_df
        insert_erc20_df(df_coins_info, blockchain)
        # Pool info
        df_dex_info = uniswap_v3_obj.dex_info_df
        insert_dex_info_df(df_dex_info,blockchain)
    
        # update the state price dictionary
        #state_price = uniswap_v3_obj.get_state_price(blocknumber = 'latest', if_block_datetime = True)
        # state price info
        #df_state_price = uniswap_v3_obj.state_price_dict
        
        

        
        print(f"Blockchain: {blockchain}")
        print(sub_df)   
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #%%
### original loop for non multicall functions
for row_num in range(len(df)):
    row = df.iloc[row_num]
    project_name = row['project_name']
    address = row['address']
    token_id = int(row['token_id'])
    blockchain = row['blockchain']
    tick_lower = int(row['tick_lower'])
    tick_upper = int(row['tick_upper'])
    if project_name == 'Uniswap_V3':
        
        tick, sqrtPriceX96,feeGrowthInsideCurrent0,feeGrowthInsideCurrent1 = \
        uniswap_v3_state_info(address, rpc_dict[blockchain], tick_lower, tick_upper, blocknumber = 'latest')
        insert_uniswap_state_info(blockchain, project_name, address, tick, sqrtPriceX96, feeGrowthInsideCurrent0, feeGrowthInsideCurrent1, token_id)
        
    if row_num % 5 == 0:
        print("Waiting 1 second...")
        time.sleep(1)    


# Optionally convert to a list of tuples
#unique_list = list(unique_combinations.itertuples(index=False, name=None))

for blockchain, sub_df in unique_combinations.groupby('blockchain'):
    
    
    
    print(f"Blockchain: {blockchain}")
    print(sub_df)
    

#%%

# optimism USDC-WBTC 3000
contract_address = "0xaDAb76dD2dcA7aE080A796F0ce86170e482AfB4a" 
blockchain = 'Optimism'
web3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))
print(web3.is_connected() )

# Uniswap V3
from class_uniswap import Uniswap_v3
uniswap_v3_obj = Uniswap_v3(contract_address, rpc_dict[blockchain])

# update the state price dictionary
state_price = uniswap_v3_obj.get_state_price(blocknumber = 'latest', if_block_datetime = True)

df_state_price = uniswap_v3_obj.state_price_dict

# ERC20 info
df_coins_info = uniswap_v3_obj.coins_info_df

# active NFT position info 
tokenID = 892282

nft_token_info_dict = uniswap_v3_obj.get_nft_token_info(tokenID)
nft_token_amount_df = uniswap_v3_obj.get_nft_token_amount()

nft_token_fee_df = uniswap_v3_obj.get_nft_token_fee()

contract_address = "0x19EA026886cbB7A900EcB2458636d72b5CaE223B" 
# active NFT position info 
tokenID = 907992
nft_token_info_dict = uniswap_v3_obj.get_nft_token_info(tokenID)
nft_token_amount_df = uniswap_v3_obj.get_nft_token_amount()
nft_token_fee_df = uniswap_v3_obj.get_nft_token_fee()

contract_address = "0x19EA026886cbB7A900EcB2458636d72b5CaE223B" 
uniswap_v3_obj = Uniswap_v3(contract_address, rpc_dict[blockchain])
# update the state price dictionary
state_price = uniswap_v3_obj.get_state_price(blocknumber = 'latest', if_block_datetime = True)
# active NFT position info 
tokenID = 975780
nft_token_info_dict = uniswap_v3_obj.get_nft_token_info(tokenID)
nft_token_amount_df = uniswap_v3_obj.get_nft_token_amount()
nft_token_fee_df = uniswap_v3_obj.get_nft_token_fee()

