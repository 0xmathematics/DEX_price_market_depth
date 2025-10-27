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
# import tqdm
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor

os.chdir('/Users/yeminlan/Documents/GitHub/DEX_Development_Kit')

#infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
#infura_url = "https://arbitrum-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90"  # arbitrum
#infura_url = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # polygon
#infura_url = 'https://base-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # base
#infura_url = 'https://linea-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # linea
#infura_url = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # optimism
infura_url = 'https://rpc.ankr.com/base' #ankr_url
#infura_url = 'https://base.llamarpc.com' #ankr_url

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.is_connected() )

# get block number/ timestamp/ datetime
block_number_current = web3.eth.block_number
block = web3.eth.get_block(block_number_current)
block_timestamp = block.timestamp
block_datetime = datetime.datetime.utcfromtimestamp(block_timestamp)
block_datetime.strftime("%Y-%m-%d %H:%M:%S")

#%%
# Uniswap V3

from class_uniswap import Uniswap_v3

# Base cbETH-WETH 0.05% pool
contract_address = "0xa9dafa443a02fbc907cb0093276b3e6f4ef02a46" 
# Base Uniswap V3 NFT
nft_address = "0x03a520b32C04BF3bEEf7BEb72E919cf822Ed34f1" 
# wallet address
wallet_address = "0x3d8d388742a2Ce2AcaF90F980e5553436a728933"
# nft tokenID
tokenID = 525361

# Arbitrum WETH-UNI 0.30% pool
contract_address = "0xC24f7d8E51A64dc1238880BD00bb961D54cbeb29" 
# Arbitrum Uniswap V3 NFT
nft_address = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88" 
# wallet address
wallet_address = "0x3d8d388742a2Ce2AcaF90F980e5553436a728933"
# nft tokenID
tokenID = 688636

# Optimism USDC-ETH 0.30% pool
contract_address = "0xc1738D90E2E26C35784A0d3E3d8A9f795074bcA4"
# Optimism Uniswap V3 NFT
nft_address = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88" 
# wallet address
wallet_address = "0xc86FD78a9d5aDe54f76c5A11FDAC1642Fa307946"
# nft tokenID
tokenID = 703220


uniswap_v3_obj = Uniswap_v3(contract_address, infura_url)
#print(uniswap_v3_obj.coins_info_df)

uniswap_v3_obj.get_state_price(blocknumber = 'latest', if_block_datetime = True)
#print(uniswap_v3_obj.state_price_dict)

uniswap_v3_obj.get_nft_token_info(tokenID = tokenID, nft_address = nft_address)
#print(uniswap_v3_obj.nft_token_info_dict)

nft_token_amount = uniswap_v3_obj.get_nft_token_amount()
nft_token_fee = uniswap_v3_obj.get_nft_token_fee()



#%%