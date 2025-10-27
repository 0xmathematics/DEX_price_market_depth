#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 06:02:28 2024

@author: Hang Miao
"""
from web3 import Web3
import datetime
import pandas as pd
import numpy as np
import json

#infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" # eth
# web3 = Web3(Web3.HTTPProvider(infura_url))
class curve_finance:
    def __init__(self,contract_address, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        web3 = self.web3
        abi = json.loads('[{"name":"Transfer","inputs":[{"type":"address","name":"sender","indexed":true},{"type":"address","name":"receiver","indexed":true},{"type":"uint256","name":"value","indexed":false}],"anonymous":false,"type":"event"},{"name":"Approval","inputs":[{"type":"address","name":"owner","indexed":true},{"type":"address","name":"spender","indexed":true},{"type":"uint256","name":"value","indexed":false}],"anonymous":false,"type":"event"},{"name":"TokenExchange","inputs":[{"type":"address","name":"buyer","indexed":true},{"type":"int128","name":"sold_id","indexed":false},{"type":"uint256","name":"tokens_sold","indexed":false},{"type":"int128","name":"bought_id","indexed":false},{"type":"uint256","name":"tokens_bought","indexed":false}],"anonymous":false,"type":"event"},{"name":"TokenExchangeUnderlying","inputs":[{"type":"address","name":"buyer","indexed":true},{"type":"int128","name":"sold_id","indexed":false},{"type":"uint256","name":"tokens_sold","indexed":false},{"type":"int128","name":"bought_id","indexed":false},{"type":"uint256","name":"tokens_bought","indexed":false}],"anonymous":false,"type":"event"},{"name":"AddLiquidity","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[2]","name":"token_amounts","indexed":false},{"type":"uint256[2]","name":"fees","indexed":false},{"type":"uint256","name":"invariant","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidity","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[2]","name":"token_amounts","indexed":false},{"type":"uint256[2]","name":"fees","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidityOne","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256","name":"token_amount","indexed":false},{"type":"uint256","name":"coin_amount","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidityImbalance","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[2]","name":"token_amounts","indexed":false},{"type":"uint256[2]","name":"fees","indexed":false},{"type":"uint256","name":"invariant","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"CommitNewAdmin","inputs":[{"type":"uint256","name":"deadline","indexed":true},{"type":"address","name":"admin","indexed":true}],"anonymous":false,"type":"event"},{"name":"NewAdmin","inputs":[{"type":"address","name":"admin","indexed":true}],"anonymous":false,"type":"event"},{"name":"CommitNewFee","inputs":[{"type":"uint256","name":"deadline","indexed":true},{"type":"uint256","name":"fee","indexed":false},{"type":"uint256","name":"admin_fee","indexed":false}],"anonymous":false,"type":"event"},{"name":"NewFee","inputs":[{"type":"uint256","name":"fee","indexed":false},{"type":"uint256","name":"admin_fee","indexed":false}],"anonymous":false,"type":"event"},{"name":"RampA","inputs":[{"type":"uint256","name":"old_A","indexed":false},{"type":"uint256","name":"new_A","indexed":false},{"type":"uint256","name":"initial_time","indexed":false},{"type":"uint256","name":"future_time","indexed":false}],"anonymous":false,"type":"event"},{"name":"StopRampA","inputs":[{"type":"uint256","name":"A","indexed":false},{"type":"uint256","name":"t","indexed":false}],"anonymous":false,"type":"event"},{"outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"name":"initialize","outputs":[],"inputs":[{"type":"string","name":"_name"},{"type":"string","name":"_symbol"},{"type":"address","name":"_coin"},{"type":"uint256","name":"_decimals"},{"type":"uint256","name":"_A"},{"type":"uint256","name":"_fee"},{"type":"address","name":"_admin"}],"stateMutability":"nonpayable","type":"function","gas":470049},{"name":"decimals","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":291},{"name":"transfer","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":75402},{"name":"transferFrom","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_from"},{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":112037},{"name":"approve","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_spender"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":37854},{"name":"get_previous_balances","outputs":[{"type":"uint256[2]","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2254},{"name":"get_balances","outputs":[{"type":"uint256[2]","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2284},{"name":"get_twap_balances","outputs":[{"type":"uint256[2]","name":""}],"inputs":[{"type":"uint256[2]","name":"_first_balances"},{"type":"uint256[2]","name":"_last_balances"},{"type":"uint256","name":"_time_elapsed"}],"stateMutability":"view","type":"function","gas":1522},{"name":"get_price_cumulative_last","outputs":[{"type":"uint256[2]","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2344},{"name":"admin_fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":621},{"name":"A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":5859},{"name":"A_precise","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":5821},{"name":"get_virtual_price","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1011891},{"name":"calc_token_amount","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"bool","name":"_is_deposit"}],"stateMutability":"view","type":"function"},{"name":"calc_token_amount","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"bool","name":"_is_deposit"},{"type":"bool","name":"_previous"}],"stateMutability":"view","type":"function"},{"name":"add_liquidity","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"uint256","name":"_min_mint_amount"}],"stateMutability":"nonpayable","type":"function"},{"name":"add_liquidity","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"uint256","name":"_min_mint_amount"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"get_dy","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"stateMutability":"view","type":"function"},{"name":"get_dy","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256[2]","name":"_balances"}],"stateMutability":"view","type":"function"},{"name":"get_dy_underlying","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"stateMutability":"view","type":"function"},{"name":"get_dy_underlying","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256[2]","name":"_balances"}],"stateMutability":"view","type":"function"},{"name":"exchange","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"}],"stateMutability":"nonpayable","type":"function"},{"name":"exchange","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"exchange_underlying","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"}],"stateMutability":"nonpayable","type":"function"},{"name":"exchange_underlying","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"remove_liquidity","outputs":[{"type":"uint256[2]","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"uint256[2]","name":"_min_amounts"}],"stateMutability":"nonpayable","type":"function"},{"name":"remove_liquidity","outputs":[{"type":"uint256[2]","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"uint256[2]","name":"_min_amounts"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"remove_liquidity_imbalance","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"uint256","name":"_max_burn_amount"}],"stateMutability":"nonpayable","type":"function"},{"name":"remove_liquidity_imbalance","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[2]","name":"_amounts"},{"type":"uint256","name":"_max_burn_amount"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"calc_withdraw_one_coin","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"int128","name":"i"}],"stateMutability":"view","type":"function"},{"name":"calc_withdraw_one_coin","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"int128","name":"i"},{"type":"bool","name":"_previous"}],"stateMutability":"view","type":"function"},{"name":"remove_liquidity_one_coin","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"int128","name":"i"},{"type":"uint256","name":"_min_received"}],"stateMutability":"nonpayable","type":"function"},{"name":"remove_liquidity_one_coin","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"_burn_amount"},{"type":"int128","name":"i"},{"type":"uint256","name":"_min_received"},{"type":"address","name":"_receiver"}],"stateMutability":"nonpayable","type":"function"},{"name":"ramp_A","outputs":[],"inputs":[{"type":"uint256","name":"_future_A"},{"type":"uint256","name":"_future_time"}],"stateMutability":"nonpayable","type":"function","gas":152464},{"name":"stop_ramp_A","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":149225},{"name":"admin_balances","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"i"}],"stateMutability":"view","type":"function","gas":3601},{"name":"withdraw_admin_fees","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":11347},{"name":"admin","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2141},{"name":"coins","outputs":[{"type":"address","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":2280},{"name":"balances","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":2310},{"name":"fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2231},{"name":"block_timestamp_last","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2261},{"name":"initial_A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2291},{"name":"future_A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2321},{"name":"initial_A_time","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2351},{"name":"future_A_time","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2381},{"name":"name","outputs":[{"type":"string","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":8813},{"name":"symbol","outputs":[{"type":"string","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":7866},{"name":"balanceOf","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":2686},{"name":"allowance","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"},{"type":"address","name":"arg1"}],"stateMutability":"view","type":"function","gas":2931},{"name":"totalSupply","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2531}]')
        address = Web3.to_checksum_address(contract_address)
        self.contract = web3.eth.contract(address = address, abi = abi )
        # ERC-20 ABI (Interface) to interact with the ERC-20 contract
        erc20_abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        list_coins_info = []
        n=0
        while True:
            try:
                dict_token_info = {}
                coin_address = self.contract.functions.coins(n).call()
                balance = self.contract.functions.balances(n).call()
                erc20_contract = web3.eth.contract(address = coin_address, abi = erc20_abi )
                
                decimals = erc20_contract.functions.decimals().call()
                name = erc20_contract.functions.name().call()
                symbol = erc20_contract.functions.symbol().call()
                
                dict_token_info['symbol'] = symbol
                dict_token_info['name'] = name
                dict_token_info['decimals'] = decimals
                dict_token_info['balance'] = balance
                dict_token_info['balance_adj'] = balance*10**(-decimals)
                dict_token_info['address'] = coin_address
                
                list_coins_info.append(dict_token_info)
                n += 1
            except Exception as e:  # Replace YourError with the specific error your function might raise
                # Stop the loop when the error occurs
                print(e )
                print( f'number of coins is {n}')
                break
        self.N = n
        self.df_coins_info = pd.DataFrame(list_coins_info)
        #self.N_coin = len(self.coin_address_list)
        self.A = self.contract.functions.A().call()/n**(n-1)
        self.swap_fee = self.contract.functions.fee().call() *10**(-10) 
        self.D = self.NM_get_D()
        
    def state_update(self, blocknumber = 'latest', if_block_datetime = False):
        n = self.N
        for i in range(n):
            balance = self.contract.functions.balances(i).call(block_identifier=blocknumber)
            decimals = self.df_coins_info['decimals'][i]
            #self.df_coins_info['balance'][i] = balance
            #self.df_coins_info['balance_adj'][i] = balance * 10.0**(-decimals)
            self.df_coins_info.loc[i, 'balance' ] = balance
            self.df_coins_info.loc[i, 'balance_adj' ] = balance * 10.0**(-decimals)
        self.D = self.NM_get_D()
        if if_block_datetime:
            block = self.web3.eth.get_block(blocknumber)
            block_timestamp = block.timestamp
            block_datetime = datetime.datetime.utcfromtimestamp(block_timestamp)
            block_datetime = block_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print( f'block number is {blocknumber} '  )
            print(f'block timestamp is {block_timestamp} '  )
            print(f'block date is {block_datetime} '   )
        
    def NM_get_D(self,  tol=1e-18, max_iter=250):
        prod_x = self.df_coins_info['balance_adj'].prod()
        sum_x = self.df_coins_info['balance_adj'].sum()
        A = self.A; n = self.N; D_0 = sum_x
        ANN = A*n**n
        prod_n_x = n**n*prod_x
        D_k = D_0
        D_next = ( ANN*sum_x+ n*D_k**(n+1)/prod_n_x)/(ANN+ (n+1)*D_k**(n)/prod_n_x-1)
        iteration = 0

        while abs(D_k-D_next) > tol and iteration < max_iter:
            D_k = D_next
            D_next = (ANN*sum_x+ n*D_k**(n+1)/prod_n_x)/(ANN+ (n+1)*D_k**(n)/prod_n_x-1)
            
            iteration += 1
        print(D_next)
        print(iteration)
        return D_next #, iteration
    
    def NM_get_Y(self, dx, i,j,   tol=1e-18, max_iter=250):
        D = self.D; A = self.A; n = self.N;
        ANN = A*n**n
        #prod_n_x = n**n*prod_x
        x_arr = np.array(self.df_coins_info['balance_adj'])
        x_arr[i] = x_arr[i] + dx
        x_0 = x_arr[j]
        x_arr = np.delete(x_arr, j)
        x_prod = x_arr.prod()
        x_k = x_0
        x_next = (D**(n+1)/ ( n**n*x_prod) + ANN*x_k**2)/(ANN*(2*x_k+x_arr.sum())-ANN*D+D )
        iteration = 0

        while abs(x_next-x_k) > tol and iteration < max_iter:
            x_k = x_next
            x_next = (D**(n+1)/ ( n**n*x_prod) + ANN*x_k**2)/(ANN*(2*x_k+x_arr.sum())-ANN*D+D )
            
            iteration += 1
        dy =  abs( x_next  -x_0 )*(1-self.swap_fee)
        #print(iteration)
        #print(dy)
        return dy
    
    def get_Y(self, dx, i_, j_):
        decimals_i = self.df_coins_info['decimals'][i_]
        decimals_j = self.df_coins_info['decimals'][j_]
        #dx_ = dx*10**decimals_i.astype(int).item()
        dx_ = dx*10**decimals_i.astype(int).item()
        
        dy = self.contract.functions.get_dy(i_,j_,dx = dx_).call()
        dy_adj = dy*10.0**(-decimals_j)
        return dy_adj  
    
    def curve_state_price(self, i, j):  # 
        D = self.D; A = self.A; n = self.N; 
        x_i = self.df_coins_info['balance_adj'][i]
        x_j = self.df_coins_info['balance_adj'][j]
        x_prod = self.df_coins_info['balance_adj'].prod()
        A_sum_con = A*n**(2*n)*x_prod*x_i*x_j
        rates_i_j =  (A_sum_con+ D**(n+1)*x_j)/(A_sum_con+ D**(n+1)*x_i)
        return rates_i_j