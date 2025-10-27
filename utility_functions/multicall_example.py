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
blockchain = 'Ethereum'
# Connect to an Ethereum node (e.g. Infura)
w3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))

# Addresses to query balances for
addresses = [
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0",
]

# Token contract (e.g. USDC contract)
token_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# ERC20 ABI fragment for balanceOf
balance_of_fn = "balanceOf(address)(uint256)"

# Create Call objects for each address
calls = [Call(token_address, balance_of_fn, [addr], [[addr, None]]) for addr in addresses]

# Create Multicall object
multi = Multicall(calls=calls, _w3=w3)

import nest_asyncio
nest_asyncio.apply()
# Execute multicall
results = multi()

# Print results
for addr, balance in results.items():
    print(f"Address: {addr}, Balance: {balance / 1e6:.2f} USDC")  # USDC has 6 decimals




#%%
from multicall import Call, Multicall

#from web3 import AsyncWeb3
#from web3.providers import AsyncHTTPProvider

blockchain = 'Ethereum'
# Use AsyncHTTPProvider instead of Web3.HTTPProvider
w3 = AsyncWeb3(AsyncHTTPProvider(rpc_dict[blockchain]))

blockchain = 'Ethereum'
web3 = Web3(Web3.HTTPProvider(rpc_dict[blockchain]))
print(web3.is_connected() )

chain_id = web3.eth.chain_id
print(chain_id)

web3.provider

web3.eth.is_async



# assuming you are on kovan
MKR_TOKEN = '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2'
MKR_WHALE = '0xdb33dfd3d61308c33c63209845dad3e6bfb2c674'
MKR_FISH = '0x2dfcedcb401557354d0cf174876ab17bfd6f4efd'

def from_wei(value):
    return value / 1e18

multi = Multicall([
    Call(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_WHALE], [('whale', from_wei)]),
    Call(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_FISH], [('fish', from_wei)]),
    Call(MKR_TOKEN, 'totalSupply()(uint256)', [('supply', from_wei)]),
], _w3=web3)

multi()  # {'whale': 566437.0921992733, 'fish': 7005.0, 'supply': 1000003.1220798912}



import nest_asyncio
nest_asyncio.apply()
aaa =  multi()

# seth-style calls
Call(MKR_TOKEN, ['balanceOf(address)(uint256)', MKR_WHALE])(_w3=web3)
Call(MKR_TOKEN, 'balanceOf(address)(uint256)')(MKR_WHALE)
# return values processing
Call(MKR_TOKEN, 'totalSupply()(uint256)', [('supply', from_wei)])()



#%%

from decimal import Decimal
from web3.datastructures import AttributeDict
from multicall import Call, Multicall


MCD_VAT = "0x35d1b3f3d7966a1dfe207aa4514c12a259a0492b"
MCD_VOW = "0xa950524441892a31ebddf91d3ceefa04bf454466"
MCD_DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
UNISWAP_EXCHANGE = "0x2a1530C4C41db0B0b2bB646CB5Eb1A67b7158667"
SAI = "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359"
MCD_JOIN_SAI = "0xad37fd42185ba63009177058208dd1be4b136e6b"
MCD_GOV = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
GEM_PIT = "0x69076e44a9C70a67D5b79d95795Aba299083c275"
ETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
MCD_JOIN_ETH_A = "0x2f0b23f53734252bda2277357e97e1517d6b042a"
BAT = "0x0d8775f648430679a709e98d2b0cb6250d2887ef"
MCD_JOIN_BAT_A = "0x3d0b1912b66114d4096f48a8cee3a56c231772ca"
MCD_POT = "0x197e90f9fad81970ba7976f33cbd77088e5d7cf7"
CDP_MANAGER = "0x5ef30b9986345249bc32d8928b7ee64de9435e39"
MCD_JUG = "0x19c0976f590d67707e62397c87829d896dc0f1f1"
MCD_FLIP_ETH_A = "0xd8a04f5412223f513dc55f839574430f5ec15531"
MCD_FLIP_BAT_A = "0xaa745404d55f88c108a28c86abe7b5a1e7817c07"
MCD_SPOT = "0x65c79fcb50ca1594b025960e539ed7a9a6d434a3"
CHAI = "0x06AF07097C9Eeb7fD685c692751D5C66dB49c215"


def from_wad(value):
    return Decimal(value) / 10**18


def from_ray(value):
    return Decimal(value) / 10**27


def from_rad(value):
    return Decimal(value) / 10**45


def from_ilk(values):
    return {
        "Art": from_wad(values[0]),
        "rate": from_ray(values[1]),
        "spot": from_ray(values[2]),
        "line": from_rad(values[3]),
        "dust": from_rad(values[4]),
    }


def from_jug(values):
    return {
        "duty": from_ray(values[0]),
        "rho": values[1],
    }


def from_spot(values):
    return {
        "pip": values[0],
        "mat": from_ray(values[1]),
    }


def calc_fee(rate):
    return rate ** (60 * 60 * 24 * 365) * 100 - 100


def get_fee(base, jug):
    return calc_fee(base + jug["duty"])


multi = Multicall(
    [
        Call(MCD_VAT, ["Line()(uint256)"], [["Line", from_rad]]),
        Call(MCD_VAT, ["debt()(uint256)"], [["debt", from_rad]]),
        Call(MCD_VAT, ["vice()(uint256)"], [["vice", from_rad]]),
        Call(MCD_VAT, ["dai(address)(uint256)", MCD_VOW], [["vow_dai", from_rad]]),
        Call(MCD_VAT, ["sin(address)(uint256)", MCD_VOW], [["vow_sin", from_rad]]),
        Call(
            MCD_VAT,
            ["ilks(bytes32)((uint256,uint256,uint256,uint256,uint256))", b"ETH-A"],
            [["eth_ilk", from_ilk]],
        ),
        Call(
            MCD_VAT,
            ["ilks(bytes32)((uint256,uint256,uint256,uint256,uint256))", b"BAT-A"],
            [["bat_ilk", from_ilk]],
        ),
        Call(
            MCD_VAT,
            ["ilks(bytes32)((uint256,uint256,uint256,uint256,uint256))", b"SAI"],
            [["sai_ilk", from_ilk]],
        ),
        Call(MCD_VOW, ["hump()(uint256)"], [["surplus_buffer", from_rad]]),
        Call(MCD_VOW, ["sump()(uint256)"], [["debt_size", from_rad]]),
        Call(MCD_VOW, ["Ash()(uint256)"], [["ash", from_rad]]),
        Call(MCD_VOW, ["Sin()(uint256)"], [["sin", from_rad]]),
        Call(MCD_DAI, ["totalSupply()(uint256)"], [["dai_supply", from_wad]]),
        Call(
            MCD_DAI,
            ["balanceOf(address)(uint256)", UNISWAP_EXCHANGE],
            [["uniswap_dai", from_wad]],
        ),
        Call(SAI, ["totalSupply()(uint256)"], [["sai_supply", from_wad]]),
        Call(
            SAI,
            ["balanceOf(address)(uint256)", MCD_JOIN_SAI],
            [["sai_locked", from_wad]],
        ),
        Call(MCD_GOV, ["balanceOf(address)(uint256)", GEM_PIT], [["gem_pit", from_wad]]),
        Call(
            ETH,
            ["balanceOf(address)(uint256)", MCD_JOIN_ETH_A],
            [["eth_locked", from_wad]],
        ),
        Call(BAT, ["totalSupply()(uint256)"], [["bat_supply", from_wad]]),
        Call(
            BAT,
            ["balanceOf(address)(uint256)", MCD_JOIN_BAT_A],
            [["bat_locked", from_wad]],
        ),
        Call(MCD_POT, ["Pie()(uint256)"], [["savings_pie", from_wad]]),
        Call(MCD_POT, ["chi()(uint256)"], [["pie_chi", from_ray]]),
        Call(MCD_POT, ["rho()(uint256)"], [["pot_drip", None]]),
        Call(MCD_POT, ["dsr()(uint256)"], [["dsr", from_ray]]),
        Call(CDP_MANAGER, ["cdpi()(uint256)"], [["cdps", None]]),
        Call(MCD_JUG, ["base()(uint256)"], [["base", from_ray]]),
        Call(
            MCD_JUG,
            ["ilks(bytes32)((uint256,uint256))", b"ETH-A"],
            [["eth_jug", from_jug]],
        ),
        Call(
            MCD_JUG,
            ["ilks(bytes32)((uint256,uint256))", b"BAT-A"],
            [["bat_jug", from_jug]],
        ),
        Call(
            MCD_JUG,
            ["ilks(bytes32)((uint256,uint256))", b"SAI"],
            [["sai_jug", from_jug]],
        ),
        Call(MCD_FLIP_ETH_A, ["kicks()(uint256)"], [["eth_kicks", None]]),
        Call(MCD_FLIP_BAT_A, ["kicks()(uint256)"], [["bat_kicks", None]]),
        Call(
            MCD_SPOT,
            ["ilks(bytes32)((address,uint256))", b"ETH-A"],
            [["eth_mat", from_spot]],
        ),
        Call(
            MCD_SPOT,
            ["ilks(bytes32)((address,uint256))", b"BAT-A"],
            [["bat_mat", from_spot]],
        ),
        Call(CHAI, ["totalSupply()(uint256)"], [["chai_supply", from_wad]]),
        Call(MCD_GOV, ["totalSupply()(uint256)"], [["mkr_supply", from_wad]]),
    ]
)


def fetch_data():
    data = multi()
    data["eth_fee"] = get_fee(data["base"], data["eth_jug"])
    data["bat_fee"] = get_fee(data["base"], data["bat_jug"])
    data["sai_fee"] = get_fee(data["base"], data["sai_jug"])
    data["pot_fee"] = calc_fee(data["dsr"])
    data["savings_dai"] = data["savings_pie"] * data["pie_chi"]
    data["eth_price"] = data["eth_mat"]["mat"] * data["eth_ilk"]["spot"]
    data["bat_price"] = data["bat_mat"]["mat"] * data["bat_ilk"]["spot"]
    data["sys_locked"] = (
        data["eth_price"] * data["eth_locked"]
        + data["bat_price"] * data["bat_locked"]
        + data["sai_locked"]
    )
    data["sys_surplus"] = data["vow_dai"] - data["vow_sin"]
    data["sys_debt"] = data["vow_sin"] - data["sin"] - data["ash"]
    return data


def main():
    data = fetch_data()
    data = AttributeDict.recursive(data)
    print("The Fundamental Equation of Dai")
    print(
        f"{data.eth_ilk.Art * data.eth_ilk.rate:,.0f} + {data.bat_ilk.Art * data.bat_ilk.rate:,.0f} + {data.sai_ilk.Art:,.0f} + {data.vice:,.0f} = {data.debt:,.0f}"
    )
    print("(Dai from ETH + Dai from BAT + Dai from Sai + System Debt) = Total Dai")
    print()
    print(f"Total Dai: {data.debt:,.0f}")
    print(f"Total Sai: {data.sai_supply:,.0f}")
    print(f"Dai + Sai: {data.debt + data.sai_supply:,.0f}")
    print(f"Total Chai: {data.chai_supply:,.0f}")
    print()
    print(
        f"Dai from ETH: {data.eth_ilk.Art * data.eth_ilk.rate:,.0f} ({data.eth_ilk.Art * data.eth_ilk.rate / data.debt:.2%})"
    )
    print(
        f"Dai from BAT: {data.bat_ilk.Art * data.bat_ilk.rate:,.0f} ({data.bat_ilk.Art * data.bat_ilk.rate / data.debt:.2%})"
    )
    print(
        f"Dai from SAI: {data.sai_ilk.Art * data.sai_ilk.rate:,.0f} ({data.sai_ilk.Art * data.sai_ilk.rate / data.debt:.2%})"
    )
    print()
    print(f"ETH Locked: {data.eth_locked:,.0f}")  # eth_supply missing
    print(
        f"ETH Ceiling: {data.eth_ilk.line:,.0f} Dai ({data.eth_ilk.Art * data.eth_ilk.rate / data.eth_ilk.line:.2%} util.)"
    )
    print(f"ETH Stability Fee: {data.eth_fee:.2f}%")
    print()
    print(f"BAT Locked: {data.bat_locked:,.0f} ({data.bat_locked / data.bat_supply:.2%} supply)")
    print(
        f"BAT Ceiling: {data.bat_ilk.line:,.0f} Dai ({data.bat_ilk.Art * data.bat_ilk.rate / data.bat_ilk.line:.2%} util.)"
    )
    print(f"BAT Stability Fee: {data.bat_fee:.2f}%")
    print()
    print(f"Dai (ERC20) Supply: {data.dai_supply:,.0f} ({data.dai_supply / data.debt:.2%})")
    print(f"Dai in DSR: {data.savings_dai:,.0f} ({data.savings_dai / data.debt:.2%})")
    print(f"Pie in DSR: {data.savings_pie:,.0f}")
    print(f"Dai Savings Rate: {data.pot_fee:.2f}%")
    print()
    print(f"ETH Price: ${data.eth_price:,.2f}")
    print(f"BAT Price: ${data.bat_price:,.4f}")
    print(f"Collat. Ratio: {data.sys_locked / data.debt:,.2%}")
    print(f"Total Locked: ${data.sys_locked:,.0f}")
    print()
    print(f"System Surplus: {data.sys_surplus:,.0f} Dai")
    print(f"Surplus Buffer: {data.surplus_buffer:,.0f}")
    print()
    print(f"Debt available to heal: {data.sys_debt:,.0f} Dai")
    print(f"Debt Buffer: {data.debt_size:,.0f}")
    print()
    print(f"Vaults Opened: {data.cdps:,d}")
    print()
    print(f"ETH Vault Auctions: {data.eth_kicks:,d}")
    print(f"BAT Vault Auctions: {data.bat_kicks:,d}")
    print()
    print(f"MKR Supply: {data.mkr_supply:,.2f}")
    print(f"MKR in Burner: {data.gem_pit:,.2f}")
    print()
    print(f"Dai in Uniswap: {data.uniswap_dai:,.0f}")


if __name__ == "__main__":
    main()