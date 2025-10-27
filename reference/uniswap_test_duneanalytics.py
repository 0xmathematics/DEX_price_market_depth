# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:04:12 2023

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





#%%
# Uniswap V3

# tx hash = 0x707bafa97e0b2c6ae78f3d77c3b21e8dce9a3abbe543f0b9d14346b301f51324

from class_uniswap import Uniswap_v3
# optimism WBTC/ETH 0.3%
contract_address = "0x73b14a78a0d396c521f954532d43fd5ffe385216" 

# optimism WETH/USDC 0.05%
contract_address = "0x85149247691df622eaf1a8bd0cafd40bc45154a9" 
 
infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
infura_url = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  # # optimism
   
uniswap_v3_obj = Uniswap_v3(contract_address, infura_url)

df_coins_info = uniswap_v3_obj.coins_info_df
fee = uniswap_v3_obj.swap_fee
state_price_dict = uniswap_v3_obj.state_price(blocknumber = 19870914, if_block_datetime = True)





#%%
import os
#os.chdir(r'/Users/yeminlan/Dropbox/python/ts/wavelets')
os.chdir(r'C:\Users\Hahn\Desktop\code\python\web3\uniswap v3')
os.chdir(r'/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/reference')
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor
import uniswap_v3_math as uni



# optimism ETH/WBTC 0.3%
# tx hash = 0x707bafa97e0b2c6ae78f3d77c3b21e8dce9a3abbe543f0b9d14346b301f51324

d0 = 18
d1 = 8

x = 0
y = 0.004

x = x*10**d0
y = 0.004*10**d1

dL = 4340988993385
ta = -262440
tb = -261540

pa = 1.0001**ta
pb = 1.0001**(tb)
#pa = uni.tick_to_price(ta,d0,d1)
#pb = uni.tick_to_price(tb,d0,d1)

L = y/(sqrt(pb) - sqrt(pa))




#%%
# optimism WETH/USDC 0.05%



# tx hash = 0xdae843887875ca6b0997c561d376d4bcaaf375de774e285154683536ab33f619
d0 = 18
d1 = 6
x = 14627461427857774
y = 200000000

dL = 30373568949621
ta = -196250
tb = -193380

pa = 1.0001**ta
pb = 1.0001**tb
pa = uni.tick_to_price(ta,d0,d1)
pb = uni.tick_to_price(tb,d0,d1)

P = y/x
L = sqrt(x*y)

## x = 0
## tx = https://arbiscan.io/tx/0x1b35cc8148a7d0428dc02b60c7d7639cc8af44406c14aa0fddb546f383b00743
x = 0
y = 797999999999998686
dL = 388312856358010
ta = 256580
tb = 256690
d0 = 8
d1 = 18
pa = 1.0001**ta
pb = 1.0001**tb

y/ ( sqrt( pb) - sqrt( pa)  )  ## equal to dL

## y = 0
## tx =  0xb80a32a799d7bf369ca2b54b8b78a5c84533cf174d1e06c9689aa551a9e0c810
x = 1724848
y = 0
dL = 259758080336129
ta = 256760
tb = 256810
d0 = 8
d1 = 18
pa = 1.0001**ta
pb = 1.0001**tb

x* ( sqrt( pb) * sqrt( pa)  )  / ( sqrt( pb) - sqrt( pa)  )  ## equal to dL

## x,y != 0
## tx =  0x5c8fc568f8d7db8b92d3867af42a5c0d39e1951d40ed1cdc76fc173399ad4ce1
x = 9860944
y = 510623461790347930
dL = 95009144914601
ta = 256310
tb = 257390
d0 = 8
d1 = 18
pa = 1.0001**ta
pb = 1.0001**tb


P = ( y/dL+sqrt(pa) )**2
# A/B
P_adjusted = P*10**(d0-d1) 
# B/A
1/P_adjusted


dL*( sqrt(P)-sqrt(pa) )        #y
dL*( 1/sqrt(P) - 1/sqrt(pb) )  #x







x* ( sqrt( pb) * sqrt( pa)  )  / ( sqrt( pb) - sqrt( pa)  )  ## equal to dL

P_adjusted = y/10**d1/(x/10**d0) 



dL*( sqrt(P) - sqrt(pa) )

dL*( 1/sqrt(P) - 1/sqrt(pb) )



dL*( sqrt(P) - sqrt(pa) )

dL*( sqrt(P) - sqrt(pa) )


y/10**d1 / ( sqrt( pb) - sqrt( pa)  )

sqrt((x/10**d0)*(y/10**d1) )
