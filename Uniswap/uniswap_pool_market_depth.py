# -*- coding: utf-8 -*-
"""
Created on May 14 16:24:40 2024

@author: Hang
"""

import os
import sys
#path_utils = r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\utility_functions'
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
path_utils = r'../utility_functions'
path_utils = '/home/hang/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)
from utils_functions import get_abi
from dotenv import load_dotenv
from privateKey import *

env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)


rpc_dict = {
    'Ethereum':os.getenv('infura_url_ethereum'),
    'Arbitrum' : os.getenv('infura_url_arbitrum') , 
    'Polygon' : os.getenv('infura_url_polygon'), 
    'Base' : os.getenv('infura_url_base'), 
    'Linea' : os.getenv('infura_url_linea') ,
    'Optimism' : os.getenv('infura_url_optimism') ,
    'Unichain' : os.getenv('infura_url_unichain') ,
    
    }
from getpass import getpass



from web3 import Web3
import numpy as np
import pandas as pd

import json
import datetime
import time
#import tqdm
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor




# set the wd to the folder
#os.chdir(r'C:\Users\Hahn\Desktop\github\DEX_Development_Kit\Uniswap')
os.chdir('/home/hang/Documents/GitHub/DEX_Development_Kit/Uniswap')
#os.chdir('/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/Uniswap')
print("Current working directory:", os.getcwd())


from class_uniswap import Uniswap_v3


'''
# get block number/ timestamp/ datetime
block_number_current = web3.eth.block_number
block = web3.eth.get_block(block_number_current)
block_timestamp = block.timestamp
block_datetime = datetime.datetime.utcfromtimestamp(block_timestamp)
block_datetime.strftime("%Y-%m-%d %H:%M:%S")
'''
#%%




#%%
# Uniswap V3
from class_uniswap import Uniswap_v3

floor(9/2)



# Base cbETH-WETH
contract_address = "0xa9dafa443a02fbc907cb0093276b3e6f4ef02a46" 

# optimism LINK-WETH
contract_address = "0x19EA026886cbB7A900EcB2458636d72b5CaE223B" 

# optimism USDC-WETH 3000
contract_address = "0xc1738D90E2E26C35784A0d3E3d8A9f795074bcA4" 

# optimism USDC-WBTC 3000
contract_address = "0xaDAb76dD2dcA7aE080A796F0ce86170e482AfB4a" 

blockchain = 'Optimism'
web3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))
print(web3.is_connected() )

# construct uniswap v3 object   
uniswap_v3_obj = Uniswap_v3(contract_address, rpc_dict[blockchain])
# ERC20 info
df_coins_info = uniswap_v3_obj.coins_info_df
# Pool info
df_dex_info = uniswap_v3_obj.dex_info_df

# update the state price dictionary
state_price = uniswap_v3_obj.get_state_price(blocknumber = 'latest', if_block_datetime = True)
# state price info
df_state_price = uniswap_v3_obj.state_price_dict




# NFT info
tokenID = 892282 # USDC WBTC optimism
nft_token_info_dict = uniswap_v3_obj.get_nft_token_info( tokenID)
token_amount_dict = uniswap_v3_obj.get_nft_token_amount()



# bitmap info
bitmap_dict, tick_indices = uniswap_v3_obj.get_bitmaps()
# market depth info
tick_list, ticks_dict, tick_liquidity_dict, dict_liquidity_distribution, x_amount, y_amount  = uniswap_v3_obj.get_market_depth()





#%% 
def position(tick: int) -> tuple[int, int]:
    # Simulate int24 range
    if tick < -2**23 or tick >= 2**23:
        raise ValueError("tick must be a signed 24-bit integer (int24)")

    # Arithmetic right shift by 8 bits
    word_pos = tick >> 8

    # Simulate 16-bit signed result
    if word_pos < -2**15 or word_pos >= 2**15:
        raise ValueError("wordPos exceeds int16 bounds")

    # Ensure the lower 8 bits are treated as unsigned (0-255)
    bit_pos = tick & 0xFF  # Equivalent to tick % 256 in unsigned
    print(f"Word {word_pos}, bit {bit_pos}")
    return word_pos, bit_pos

def reverse_position(word_pos: int, bit_pos: int) -> int:
    # Validate input ranges
    if word_pos < -2**15 or word_pos >= 2**15:
        raise ValueError("word_pos must be a 16-bit signed integer")
    if bit_pos < 0 or bit_pos >= 2**8:
        raise ValueError("bit_pos must be an 8-bit unsigned integer")

    tick = (word_pos << 8) | bit_pos

    # Reconstruct int24 signed value (handle negative values correctly)
    if tick >= 2**23:
        tick -= 2**24

    return tick

def iterate_bitmap_bits(start_word, start_bit, end_word, end_bit):
    current_word = start_word
    while current_word <= end_word:
        # Determine bit range for current word
        bit_start = start_bit if current_word == start_word else 0
        bit_end = end_bit if current_word == end_word else 255

        for bit_pos in range(bit_start, bit_end + 1):
            #print( current_word, bit_pos)
            print(f"Word {current_word}, bit {bit_pos}")
            tick = word_pos * 256 * tick_spacing + (bit_pos * tick_spacing)
            #tick_2 = reverse_position(word_pos,bit_pos)
            print(tick)

        current_word += 1


import bisect
def extract_sublist_range(lst, start, end):
    if start > end:
        start, end = end, start  # Ensure proper order

    start_index = bisect.bisect_left(lst, start)
    end_index = bisect.bisect_right(lst, end)
    return lst[start_index:end_index]



tick = 85176



position(tick)
2**16 2**8
1 << 8
2344>>8
2344//2**8

2**23
word_pos = tick >> 8 # or tick // 2**8
bit_pos = tick % 256
print(f"Word {word_pos}, bit {bit_pos}")

mask = 2**bit_pos # or 1 << bit_pos
print(format(mask, '#0258b'))       


#%%