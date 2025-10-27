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
path_utils = r'../utility_functions'
#path_utils ='/Users/yeminlan/Documents/GitHub/DEX_Development_Kit/utility_functions'
sys.path.append(path_utils)

from dotenv import load_dotenv
env_path = path_utils + '/config.env'
load_dotenv(dotenv_path = env_path)

ETHERSCAN_API_KEY = os.getenv('etherscan_api_key')  
OPTIMISM_API_KEY = os.getenv('opscan_api_key')  

dict_api_key = {
    'Ethereum':ETHERSCAN_API_KEY,
    'Optimism':OPTIMISM_API_KEY,
    
    }

# API doc https://docs.optimism.etherscan.io/api-endpoints/contracts
dict_url_head = {
    'Ethereum':'https://api.etherscan.io/api',
    'Optimism':'https://api-optimistic.etherscan.io/api',
    
    }


def get_abi(contract_address, blockchain='Ethereum',abi_json = True):
    api_key = dict_api_key[blockchain]
    url_param = f"?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
    url = dict_url_head[blockchain]+url_param
    response = requests.get(url)
    abi_json = response.json()['result']
    abi_list = json.loads(abi_json)
    
    if abi_json:
        return abi_json
    
    else:
        return abi_list
    
#%%

#%%


# SOL/Fartcoin
def deposit_fee(x0,x1 ):
    x0 = 0.031345556
    x1 = 5.848173
    
    decimal0 = 9
    decimal1 = 6
    Pa = 106.045418
    Pb = 319.837251
    P = 126.534998039
    pa = sqrt( Pa*10**(decimal1-decimal0))
    pb = sqrt( Pb*10**(decimal1-decimal0))
    p = sqrt( P*10**(decimal1-decimal0))
    
    
    
    aaa = p*pb/(pb-p)*(p-pa)*10**(decimal0-decimal1)
    
    dx = (x1-x0*aaa)/(aaa+P)
    
    print( dx)
    print( dx*P)
    print( x0+dx)
    print( x1-dx*P)  
    
       
    
    x0 = 1
    x1 = 0
    
    decimal0 = 18
    decimal1 = 6
    Pa = 1665.7517
    Pb = 3203.4994
    P = 1843.91 
    pa = sqrt( Pa*10**(decimal1-decimal0))
    pb = sqrt( Pb*10**(decimal1-decimal0))
    p = sqrt( P*10**(decimal1-decimal0))
    
    
    
    aaa = p*pb/(pb-p)*(p-pa)*10**(decimal0-decimal1)
    
    dx = (x1-x0*aaa)/(aaa+P)
    
    print( dx)
    print( dx*P)
    print( x0+dx)
    print( x1-dx*P)  
    
    
    
    
    
    # example WETH/USDC
    x0 = 12
    decimal0 = 18
    decimal1 = 6
    Pa = 1665.7517
    Pb = 3203.4994
    P = 1843.91
    pa = sqrt( Pa*10**(decimal1-decimal0))
    pb = sqrt( Pb*10**(decimal1-decimal0))
    p = sqrt( P*10**(decimal1-decimal0))
    
    dx = 0.829687549854441*10**(decimal0)
    Lx = dx*p*pb/(pb-p)
    dy = Lx*(p-pa)*10**(-decimal1)
    
    dy = 333*10**(decimal1)
    Ly = dy/(p-pa)
    dx = Ly*(pb-p)/(p*pb)*10**(-decimal0)





#%%









'''
################
# example
################



# Uniswap V3 NFT manager on ethereum
contract ='0xC36442b4a4522E871399CD717aBDD847Ab11FE88'
abi = get_abi(contract)

type(abi)
'''