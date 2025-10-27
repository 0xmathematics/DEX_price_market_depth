# -*- coding: utf-8 -*-
"""
Created on May 14 16:24:40 2024

@author: Hang
"""


import os
from web3 import Web3
import numpy as np
import pandas as pd
import json
import datetime
import time
import tqdm
import sys

os.chdir('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit')
sys.path.append(os.path.abspath('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/Uniswap'))
sys.path.append(os.path.abspath('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/Curve'))


infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
infura_url = "https://arbitrum-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90"  # arbitrum
infura_url = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # polygon
infura_url = 'https://base-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # base
infura_url = 'https://linea-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # linea
infura_url = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # optimism
infura_url = 'https://rpc.ankr.com/base' #ankr_url
infura_url = 'https://base.llamarpc.com' #ankr_url

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.is_connected() )

# get block number/ timestamp/ datetime
block_number_current = web3.eth.block_number
block = web3.eth.get_block(block_number_current)
block_timestamp = block.timestamp
block_datetime = datetime.datetime.utcfromtimestamp(block_timestamp)
block_datetime.strftime("%Y-%m-%d %H:%M:%S")


#block = web3.eth.get_block(20777992)

#%%
# Uniswap V2
from class_uniswap import Uniswap_v2
infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth

# # ethereum PEPE-WETH
contract_address = "0xa43fe16908251ee70ef74718545e4fe6c5ccec9f"

# # ethereum LUSD-WETH
contract_address = "0xf20ef17b889b437c151eb5ba15a47bfc62bff469"

# # base MIM-WETH
contract_address = "0x07D5695a24904CC1B6e3bd57cC7780B90618e3c4"

uniswap_v2_obj = Uniswap_v2(contract_address, infura_url)

state_price_dict = uniswap_v2_obj.state_price(blocknumber = 19869184, if_block_datetime = True)

df_coins_info = uniswap_v2_obj.df_coins_info

#%%
# Sushiswap V1
from class_sushiswap import Sushiswap_v1
infura_url = "https://arbitrum-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90"  # arbitrum


# # arbitrum MIM-WETH
contract_address = "0xb6DD51D5425861C808Fd60827Ab6CFBfFE604959"


sushiswap_v1_obj = Sushiswap_v1(contract_address, infura_url)

state_price_dict = sushiswap_v1_obj.state_price(blocknumber = 211281363, if_block_datetime = True)

df = pd.read_csv('pool_state_combined.csv')


df_red = df[df['chainId'] == df['processBlockChainId']]

df_red.to_csv('pool_state_combined_reduced.csv')


df_red_wstETH = df_red [ df_red['poolAddress'] == '0x109830a1aaad605bbf02a9dfa7b0b92ec2fb7daa']


df_red_wstETH.to_csv('wstETH.csv')

#%%
# Balancer V2
sys.path.append(os.path.abspath('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/Balancer'))

from class_balancer import balancer_v2_stable
infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
# # ETH wstETH-WETH
contract_address = "0x93d199263632a4ef4bb438f1feb99e57b4b5f0bd"  

    
Bal_v2_obj = balancer_v2_stable(contract_address, infura_url)  
df = Bal_v2_obj.df_coins_info

Bal_v2_obj.state_update( blocknumber =19870914 ,if_block_datetime = True )
df = Bal_v2_obj.df_coins_info

Bal_v2_obj.curve_state_price(1,0)
Bal_v2_obj.curve_state_price(0,1)

#%%
# Uniswap V3

from class_uniswap import Uniswap_v3
contract_address = "0x109830a1aaad605bbf02a9dfa7b0b92ec2fb7daa"  
infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
    
uniswap_v3_obj = Uniswap_v3(contract_address, infura_url)

df_coins_info = uniswap_v3_obj.coins_info_df

block_number_current = web3.eth.block_number

state_price_dict = uniswap_v3_obj.get_state_price(blocknumber = block_number_current, if_block_datetime = True)

uniswap_v3_obj.state_price_dict

#%%
# Curve 

sys.path.append(os.path.abspath('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/Curve'))


from class_curve import curve_finance     
    

# # ETH crvUSD-USDC
contract_address = "0x4dece678ceceb27446b35c672dc7d61f30bad69e" 
# # ETH 3pool
contract_address = "0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7" 
 
infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
    
crv_obj = curve_finance(contract_address, infura_url)

df_coins_info = crv_obj.df_coins_info
block_number_current = 20428298
crv_obj.state_update( blocknumber =block_number_current ,if_block_datetime = True )
df_coins_info_new = crv_obj.df_coins_info

crv_obj.curve_state_price(1,0)
crv_obj.curve_state_price(0,1)



