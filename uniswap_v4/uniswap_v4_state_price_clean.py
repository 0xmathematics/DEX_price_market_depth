#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:03:12 2025

@author: Hang Miao
"""

import os
from web3 import Web3
import numpy as np
import pandas as pd
import json
import datetime
import time
from math import sqrt, pi


#%%

####################################################
#  Uniswap V4 
####################################################

# token_info() function retrieve the token information for any given PoolID
# PoolID is the identification for different pools in Uniswap V4.
# token info function only need to run once for each specific pools

def token_info(pool_id, blockchain_name, rpc_url):
    
    # input 1: pool_id, uniswap v4 identify each individual pool using pool_id
    # input 2: blockchain_name, specify blockchain name in the following list:
    #           ['BSC', 'avalanche', 'ethereum', 'base', 'optimism', 'polygon', 'arbitrum', \
    #           'unichain', 'zora', 'blast', 'worldchain', 'ink', 'soneium']
    # input 3: rpc_url, rpc associated with the blockchain
    
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    print( web3.is_connected() )   
    
    contract_address = {
        "BSC": "0x7a4a5c919ae2541aed11041a1aeee68f1287f95b",
        "avalanche": "0xb74b1f14d2754acfcbbe1a221023a5cf50ab8acd",
        "ethereum": "0xbD216513d74C8cf14cf4747E6AaA6420FF64ee9e", 
        "base": "0x7c5f5a4bbd8fd63184577525326123b519429bdc",  
        "optimism": "0x3c3ea4b57a46241e54610e5f022e5c45859a1017",  
        "polygon": "0x1ec2ebf4f37e7363fdfe3551602425af0b3ceef9",  
        "arbitrum": "0xd88f38f930b7952f2db2432cb002e7abbf3dd869",  
        "unichain": "0x4529a01c7a0410167c5740c487a8de60232617bf",
        "zora": "	0xf66c7b99e2040f0d9b326b3b7c152e9663543d63",
        "blast": "0x12a88ae16f46dce4e8b15368008ab3380885df30",
        "worldchain": "0xc585e0f504613b5fbf874f21af14c65260fb41fa",
        "ink": "0x1b35d13a2e2528f192637f14b05f0dc0e7deb566",
        "soneium": "0x1b35d13a2e2528f192637f14b05f0dc0e7deb566",
    }
    abi_1 = json.loads('[{"inputs":[{"internalType":"contract IPoolManager","name":"_poolManager","type":"address"},{"internalType":"contract IAllowanceTransfer","name":"_permit2","type":"address"},{"internalType":"uint256","name":"_unsubscribeGasLimit","type":"uint256"},{"internalType":"contract IPositionDescriptor","name":"_tokenDescriptor","type":"address"},{"internalType":"contract IWETH9","name":"_weth9","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"subscriber","type":"address"}],"name":"AlreadySubscribed","type":"error"},{"inputs":[{"internalType":"address","name":"subscriber","type":"address"},{"internalType":"bytes","name":"reason","type":"bytes"}],"name":"BurnNotificationReverted","type":"error"},{"inputs":[],"name":"ContractLocked","type":"error"},{"inputs":[{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"DeadlinePassed","type":"error"},{"inputs":[{"internalType":"Currency","name":"currency","type":"address"}],"name":"DeltaNotNegative","type":"error"},{"inputs":[{"internalType":"Currency","name":"currency","type":"address"}],"name":"DeltaNotPositive","type":"error"},{"inputs":[],"name":"GasLimitTooLow","type":"error"},{"inputs":[],"name":"InputLengthMismatch","type":"error"},{"inputs":[],"name":"InsufficientBalance","type":"error"},{"inputs":[],"name":"InvalidContractSignature","type":"error"},{"inputs":[],"name":"InvalidEthSender","type":"error"},{"inputs":[],"name":"InvalidSignature","type":"error"},{"inputs":[],"name":"InvalidSignatureLength","type":"error"},{"inputs":[],"name":"InvalidSigner","type":"error"},{"inputs":[{"internalType":"uint128","name":"maximumAmount","type":"uint128"},{"internalType":"uint128","name":"amountRequested","type":"uint128"}],"name":"MaximumAmountExceeded","type":"error"},{"inputs":[{"internalType":"uint128","name":"minimumAmount","type":"uint128"},{"internalType":"uint128","name":"amountReceived","type":"uint128"}],"name":"MinimumAmountInsufficient","type":"error"},{"inputs":[{"internalType":"address","name":"subscriber","type":"address"},{"internalType":"bytes","name":"reason","type":"bytes"}],"name":"ModifyLiquidityNotificationReverted","type":"error"},{"inputs":[],"name":"NoCodeSubscriber","type":"error"},{"inputs":[],"name":"NoSelfPermit","type":"error"},{"inputs":[],"name":"NonceAlreadyUsed","type":"error"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"NotApproved","type":"error"},{"inputs":[],"name":"NotPoolManager","type":"error"},{"inputs":[],"name":"NotSubscribed","type":"error"},{"inputs":[],"name":"PoolManagerMustBeLocked","type":"error"},{"inputs":[],"name":"SignatureDeadlineExpired","type":"error"},{"inputs":[{"internalType":"address","name":"subscriber","type":"address"},{"internalType":"bytes","name":"reason","type":"bytes"}],"name":"SubscriptionReverted","type":"error"},{"inputs":[],"name":"Unauthorized","type":"error"},{"inputs":[{"internalType":"uint256","name":"action","type":"uint256"}],"name":"UnsupportedAction","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"subscriber","type":"address"}],"name":"Subscription","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"subscriber","type":"address"}],"name":"Unsubscription","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"contract IWETH9","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPoolAndPositionInfo","outputs":[{"components":[{"internalType":"Currency","name":"currency0","type":"address"},{"internalType":"Currency","name":"currency1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"},{"internalType":"contract IHooks","name":"hooks","type":"address"}],"internalType":"struct PoolKey","name":"poolKey","type":"tuple"},{"internalType":"PositionInfo","name":"info","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getPositionLiquidity","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"Currency","name":"currency0","type":"address"},{"internalType":"Currency","name":"currency1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"},{"internalType":"contract IHooks","name":"hooks","type":"address"}],"internalType":"struct PoolKey","name":"key","type":"tuple"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initializePool","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"unlockData","type":"bytes"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"modifyLiquidities","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes","name":"actions","type":"bytes"},{"internalType":"bytes[]","name":"params","type":"bytes[]"}],"name":"modifyLiquiditiesWithoutUnlock","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"msgSender","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextTokenId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"word","type":"uint256"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"bitmap","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"owner","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"permit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"components":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint160","name":"amount","type":"uint160"},{"internalType":"uint48","name":"expiration","type":"uint48"},{"internalType":"uint48","name":"nonce","type":"uint48"}],"internalType":"struct IAllowanceTransfer.PermitDetails","name":"details","type":"tuple"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"sigDeadline","type":"uint256"}],"internalType":"struct IAllowanceTransfer.PermitSingle","name":"permitSingle","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"permit","outputs":[{"internalType":"bytes","name":"err","type":"bytes"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"permit2","outputs":[{"internalType":"contract IAllowanceTransfer","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"components":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint160","name":"amount","type":"uint160"},{"internalType":"uint48","name":"expiration","type":"uint48"},{"internalType":"uint48","name":"nonce","type":"uint48"}],"internalType":"struct IAllowanceTransfer.PermitDetails[]","name":"details","type":"tuple[]"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"sigDeadline","type":"uint256"}],"internalType":"struct IAllowanceTransfer.PermitBatch","name":"_permitBatch","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"permitBatch","outputs":[{"internalType":"bytes","name":"err","type":"bytes"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"permitForAll","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes25","name":"poolId","type":"bytes25"}],"name":"poolKeys","outputs":[{"internalType":"Currency","name":"currency0","type":"address"},{"internalType":"Currency","name":"currency1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"},{"internalType":"contract IHooks","name":"hooks","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolManager","outputs":[{"internalType":"contract IPoolManager","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"positionInfo","outputs":[{"internalType":"PositionInfo","name":"info","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"revokeNonce","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"newSubscriber","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"subscribe","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"subscriber","outputs":[{"internalType":"contract ISubscriber","name":"subscriber","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenDescriptor","outputs":[{"internalType":"contract IPositionDescriptor","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],"name":"unlockCallback","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"unsubscribe","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"unsubscribeGasLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    abi_2 = json.loads("[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_l2Bridge\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_l1Token\",\"type\":\"address\"},{\"internalType\":\"string\",\"name\":\"_name\",\"type\":\"string\"},{\"internalType\":\"string\",\"name\":\"_symbol\",\"type\":\"string\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"_account\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"Burn\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"_account\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"Mint\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_from\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"burn\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"subtractedValue\",\"type\":\"uint256\"}],\"name\":\"decreaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"addedValue\",\"type\":\"uint256\"}],\"name\":\"increaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"l1Token\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"l2Bridge\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"mint\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes4\",\"name\":\"_interfaceId\",\"type\":\"bytes4\"}],\"name\":\"supportsInterface\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"sender\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]")

    truncated_hex = pool_id[2:52]  # keep "0x" + 50 characters
    bytes25_val = bytes.fromhex(truncated_hex)
    
    address = Web3.to_checksum_address(contract_address[blockchain_name])
    contract = web3.eth.contract( address = address, abi = abi_1 )
    
    address0, address1, fee, tickSpacing, hooks \
        = contract.functions.poolKeys(bytes25_val).call()
    token_0 ={} 
    if address0 != '0x0000000000000000000000000000000000000000':           
        address0 = Web3.to_checksum_address(address0)
        contract = web3.eth.contract( address = address0, abi = abi_2 )
        token_0['decimals'] = contract.functions.decimals().call()
        token_0['symbol'] = contract.functions.symbol().call()
    else:
        token_0['decimals'] = 18
        token_0['symbol'] = 'ETH'
        
    token_1 ={} 
    if address1 != '0x0000000000000000000000000000000000000000':  
        address1 = Web3.to_checksum_address(address1)
        contract = web3.eth.contract( address = address1, abi = abi_2 )
        token_1['decimals'] = contract.functions.decimals().call()
        token_1['symbol'] = contract.functions.symbol().call()
    else:
        token_1['decimals'] = 18
        token_1['symbol'] = 'ETH'
        
    dict_token_info ={}
    dict_token_info['token_0'] = token_0
    dict_token_info['token_1'] = token_1
    
    return dict_token_info 
    


# state_price() function retrieve the state price for the state price for each uniswap v4 pool given PoolID
# state_price() function supposed to be run every block to get the latest price information
# the output includes both state price for token0/token1 and state price for token1/token0
# For token0/token1, token0 is base and token1 is quote.
# For token1/token0, token1 is base and token0 is quote.

def state_price(pool_id, blockchain_name, dict_token_info, rpc_url):
    
    # input 1: pool_id, uniswap v4 identify each individual pool using pool_id
    # input 2: blockchain_name, specify blockchain name in the following list:
    #           ['BSC', 'avalanche', 'ethereum', 'base', 'optimism', 'polygon', 'arbitrum', \
    #           'unichain', 'zora', 'blast', 'worldchain', 'ink', 'soneium']
    # input 3: dict_token_info, dictionary of token information gotten from above token_info() function
    # input 4: rpc_url
    
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    print( web3.is_connected() )  
    
    contract_address = {
        "BSC": "0xd13dd3d6e93f276fafc9db9e6bb47c1180aee0c4",
        "avalanche": "0xc3c9e198c735a4b97e3e683f391ccbdd60b69286",
        "ethereum": "0x7fFE42C4a5DEeA5b0feC41C94C136Cf115597227", 
        "base": "0xa3c0c9b65bad0b08107aa264b0f3db444b867a71",  
        "optimism": "0xc18a3169788F4F75A170290584ECA6395C75Ecdb",  
        "polygon": "0x5ea1bd7974c8a611cbab0bdcafcb1d9cc9b3ba5a",  
        "arbitrum": "0x76fd297e2d437cd7f76d50f01afe6160f86e9990",  
        "unichain": "0x86e8631A016F9068C3f085fAF484Ee3F5fDee8f2",
        "zora": "0x385785af07d63b50d0a0ea57c4ff89d06adf7328",
        "blast": "0x12a88ae16f46dce4e8b15368008ab3380885df30",
        "worldchain": "0x51d394718bc09297262e368c1a481217fdeb71eb",
        "ink": "0x76fd297e2d437cd7f76d50f01afe6160f86e9990",
        "soneium": "0x76fd297e2d437cd7f76d50f01afe6160f86e9990",
    }

    abi = json.loads('[{"inputs":[{"internalType":"contract IPoolManager","name":"_poolManager","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"}],"name":"getFeeGrowthGlobals","outputs":[{"internalType":"uint256","name":"feeGrowthGlobal0","type":"uint256"},{"internalType":"uint256","name":"feeGrowthGlobal1","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],"name":"getFeeGrowthInside","outputs":[{"internalType":"uint256","name":"feeGrowthInside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1X128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"}],"name":"getLiquidity","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"bytes32","name":"positionId","type":"bytes32"}],"name":"getPositionInfo","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"bytes32","name":"salt","type":"bytes32"}],"name":"getPositionInfo","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"bytes32","name":"positionId","type":"bytes32"}],"name":"getPositionLiquidity","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"}],"name":"getSlot0","outputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint24","name":"protocolFee","type":"uint24"},{"internalType":"uint24","name":"lpFee","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"int16","name":"tick","type":"int16"}],"name":"getTickBitmap","outputs":[{"internalType":"uint256","name":"tickBitmap","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"int24","name":"tick","type":"int24"}],"name":"getTickFeeGrowthOutside","outputs":[{"internalType":"uint256","name":"feeGrowthOutside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"int24","name":"tick","type":"int24"}],"name":"getTickInfo","outputs":[{"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128","name":"liquidityNet","type":"int128"},{"internalType":"uint256","name":"feeGrowthOutside0X128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"PoolId","name":"poolId","type":"bytes32"},{"internalType":"int24","name":"tick","type":"int24"}],"name":"getTickLiquidity","outputs":[{"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128","name":"liquidityNet","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolManager","outputs":[{"internalType":"contract IPoolManager","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')

    address = Web3.to_checksum_address(contract_address[blockchain_name])
    contract = web3.eth.contract( address = address, abi = abi )
    
    sqrtPrice, liquidity,feeGrowthGlobal0X128, feeGrowthGlobal1X128 \
        = contract.functions.getSlot0(pool_id).call()
        
    decimals_0 = dict_token_info['token_0']['decimals']
    symbol_0 = dict_token_info['token_0']['symbol']
    decimals_1 = dict_token_info['token_1']['decimals']
    symbol_1 = dict_token_info['token_1']['symbol']
    
    
    state_price = (sqrtPrice/2**96)**2*10**(decimals_0-decimals_1)
    
    dict_state_price = {}
    dict_state_price[f'{symbol_0}/{symbol_1}'] = state_price
    dict_state_price[f'{symbol_1}/{symbol_0}'] = 1/state_price
    
    return dict_state_price
    
    



#%%

####################################################
# Examples
####################################################

################
# sUSDe/USDC
################

pool_id = "0xbe32cb3aedbf3740bbd0086831f34f882fad82c0b3c8e38ad34b524cd685b97e"
blockchain_name = 'ethereum'
rpc_url = " input ethereum rpc url here " 

# get token information from pool 
dict_token_info = token_info(pool_id, blockchain_name, rpc_url) 

# get state price from pool 
dict_state_price = state_price(pool_id, blockchain_name, dict_token_info, rpc_url) 


################
# USDe/USDT
################

pool_id = "0xba237801c29850b7ec134aa77d19855d48f9e01dee08f21945502c2a8b377e16"
blockchain_name = 'ethereum'
rpc_url = " input ethereum rpc url here " 

# get token information from the pool of interest 
dict_token_info = token_info(pool_id, blockchain_name, rpc_url) 

# get state price from pool 
dict_state_price = state_price(pool_id, blockchain_name, dict_token_info, rpc_url) 


################
# ETH/wstETH
################
pool_id = "0xd10d359f50ba8d1e0b6c30974a65bf06895fba4bf2b692b2c75d987d3b6b863d"
blockchain_name = 'unichain'
rpc_url = " input unichain rpc url here " 

# get token information from the pool of interest 
dict_token_info = token_info(pool_id, blockchain_name, rpc_url) 

# get state price from pool 
dict_state_price = state_price(pool_id, blockchain_name, dict_token_info, rpc_url) 


    
