# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:26:36 2025

@author: Hang
"""

import sys
#path_utils = 'C:\\Users\\Hahn\\Desktop\\github\\DEX_Development_Kit\\utility_functions'

path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)


import os
from web3 import Web3
import numpy as np
import pandas as pd
import json
import datetime
import time
#import tqdm
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor
from dotenv import load_dotenv
from privateKey import *
from getpass import getpass

# set the wd to the folder
# os.chdir('C:\Users\Hahn\Desktop\github\DEX_Development_Kit\Uniswap')
print("Current working directory:", os.getcwd())

env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)

rpc_url_ethereum = os.getenv('infura_url_ethereum') 
rpc_url_arbitrum = os.getenv('infura_url_arbitrum')  
rpc_url_polygon = os.getenv('infura_url_polygon') 
rpc_url_base = os.getenv('infura_url_base') 
rpc_url_linea = os.getenv('infura_url_linea') 
rpc_url_optimism = os.getenv('infura_url_optimism') 
rpc_url_unichain = os.getenv('infura_url_unichain') 

web3 = Web3(Web3.HTTPProvider(rpc_url_optimism))
print(web3.is_connected() )




#%%
## send crypto currency
account_1 = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'
account_2 = '0x98c14FE86670a4CA0300947107E6480B62dD20b8' 
account_3 = '0x46d092ea915fB9735b3d8b8d1b8CE2ba5A207a92' # mexc
#account_3 = Web3.to_checksum_address(account_3)

password = getpass("enter the password: \n")
primary_private_key = primary_privateKey( str.encode(password) )
private_key = privateKey( str.encode(password) )
private_key_acount1 = privateKey_Account1( str.encode(password) )
clear;



balance_wei_1 = web3.eth.get_balance( account_1 )
balance_wei_2 = web3.eth.get_balance( account_2 )
balance_wei_3 = web3.eth.get_balance( account_3 )
#balance_eth = web3.from_wei(balance_wei, 'ether')
print("ether balance in acount_1 is: ", web3.from_wei(balance_wei_1,'ether'))
print("ether balance in acount_2 is: ", web3.from_wei(balance_wei_2,'ether'))
print("ether balance in acount_3 is: ", web3.from_wei(balance_wei_3,'ether'))

#%%

def transfer_ETH(value_in_ether, sender_address, receiver_address,\
                  sender_private_key, gasPrice_gwei = '0.001'):


    # Get the nonce (transaction count for the sender)
    nonce = web3.eth.get_transaction_count(sender_address)
    
    # Retrieve the chain ID
    chain_id = web3.eth.chain_id
    print(f"Chain ID: {chain_id}") # Optimism Mainnet 10

    ## build the transaction
    tx = {
          'nonce': nonce,
          'to': receiver_address,
          'value': web3.to_wei(value_in_ether,'ether'),
          'gas': 21000,
          'gasPrice': web3.to_wei(gasPrice_gwei,'gwei'),
          'chainId': chain_id      
    }
    ## sign the transaction
    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, sender_private_key)
    

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_hash_hex_str = web3.to_hex(tx_hash)
    http_url = 'https://optimistic.etherscan.io/tx/'
    url = http_url+tx_hash_hex_str
    print(url)
    
    
## test send crypto currency
sender_address = account_1
receiver_address = account_2
sender_private_key = primary_private_key

#calculate the gas fee
########################
# Current Gas Price
########################
gasPrice_wei = web3.eth.gas_price
gasPrice_gwei = web3.from_wei(gasPrice_wei,'gwei')
print(gasPrice_gwei )
    
transfer_ETH(0.01, sender_address, receiver_address,\
                    sender_private_key, gasPrice_gwei)  
    
## send the transaction

## get the transaction Hash