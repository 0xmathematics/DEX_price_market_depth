#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:18:39 2025

@author: hang.miaosmartcontract.com
"""



##################
# bash
##################

'''
 curl -X POST https://api.hyperliquid.xyz/info  \
    -H "Content-Type: application/json" \
    -d '{"type": "allMids"}'
    
'''



##################
# python request
##################
import requests

url = "https://api.hyperliquid.xyz/info"

session = requests.Session()
session.headers.update({"Content-Type": "application/json"})
payload = {"type": "allMids"}
response = session.post(url, json=payload, timeout=None)
response.json()

##################
# official package
##################
from hyperliquid.info import Info
from hyperliquid.utils import constants


# pip install hyperliquid-python-sdk

# Create Info client (skip_ws=True disables websocket connection)
info = Info(constants.MAINNET_API_URL, skip_ws=True)

# Official helper method (available in recent SDK builds)
all_mids = info.all_mids()


#%%

##################
# bash
##################

'''
 curl -X POST https://api.hyperliquid.xyz/info  \
    -H "Content-Type: application/json" \
    -d '{"type": "l2Book", "coin": "ETH", "nSigFigs": 2}'
    
'''


##################
# python request
##################
import requests

url = "https://api.hyperliquid.xyz/info"


session = requests.Session()
session.headers.update({"Content-Type": "application/json"})
payload = {"type": "l2Book", "coin": 'ETH', "nSigFigs": 2}
response = session.post(url, json=payload, timeout=None)
response.json()


##################
# official package
##################
# Connect to mainnet (use TESTNET_API_URL for testnet)
info = Info(constants.MAINNET_API_URL, skip_ws=True)

# Fetch L2 order book snapshot for a given market
coin = "BTC"

orderbook = info.l2_snapshot(coin)

print(orderbook)
info.name_to_coin['SUPER']

info.coin_to_asset

# Print result
print(response)




#%%
import asyncio
from hl import Api

async def get_state_price(base = 'ETH'):
    # Initialize API without authentication for public endpoints
    api = await Api.create()

    # Get current mid prices for all assets
    result = await api.info.all_mids()

    if result.is_ok():
        mids = result.unwrap()
        #for asset, price in mids.items():
            #print(f"{asset}: ${price}")
    else:
        print(f"Error: {result.unwrap_err()}")
    return mids[base]
#asyncio.run(get_market_data())

state_price = await get_state_price()





#%%

async def get_orderbook(base = 'ETH'):
    # Initialize API without authentication for public endpoints
    api = await Api.create()

    # Get current mid prices for all assets
    
    
    result = await api.info.l2_book(asset=base, n_sig_figs=2)
    if result.is_ok():
        book = result.unwrap()
        print(f"ETH order book: {book}")
    

    else:
        print(f"Error: {result.unwrap_err()}")
    return book
#asyncio.run(get_market_data())

OB = await get_orderbook('BTC')

#%%
import pandas as pd


def OB_MD(OB,state_price):

    
    bids = OB['levels'][0]
    asks = OB['levels'][1]
    

    df_bids = pd.DataFrame(bids)
    df_asks = pd.DataFrame(asks)
    # Convert numeric columns to float
    df_bids['px'] = df_bids['px'].astype(float)
    df_bids['sz'] = df_bids['sz'].astype(float)
    df_asks['px'] = df_asks['px'].astype(float)
    df_asks['sz'] = df_asks['sz'].astype(float)

    
    upper = float(state_price)*1.01
    lower = float(state_price)*0.99
    
    MD_bids = df_bids.loc[df_bids['px']>lower]['sz'].sum()
    MD_asks = df_asks.loc[df_bids['px']<upper]['sz'].sum()
    
    return df_bids, df_asks, MD_bids, MD_asks

df_bids, df_asks, MD_bids, MD_asks = OB_MD(OB, state_price)


df_bids, df_asks, MD_bids, MD_asks = OB_MD(orderbook, state_price)


