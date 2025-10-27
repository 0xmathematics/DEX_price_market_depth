# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:44:11 2024

@author: Hang
"""
#import dotenv
from requests import get, post
import requests
import pandas as pd
import json

import os
#os.chdir(r'C:\Users\Hahn\Desktop\code\CL_DEX\analysis')
os.chdir(r'/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/Dune Analytics')
###################################################
# Download by the API provided by Dune Analytics Websites
###################################################
4mtutuc5rXoTQCzNnSZR87uvWQCdTbad  
kF8HdV0kmJVz8H1qW7JTtwTCEkdp4Nmj
yYJJytazAM8XFPFpt7dMZf4UJDOaxq5m # playground
url = 'https://api.dune.com/api/v1/query/4007751/results?api_key=4mtutuc5rXoTQCzNnSZR87uvWQCdTbad'
url = 'https://api.dune.com/api/v1/query/3999713/results?api_key=4mtutuc5rXoTQCzNnSZR87uvWQCdTbad'

url = 'https://api.dune.com/api/v1/query/3411820/results?api_key=yYJJytazAM8XFPFpt7dMZf4UJDOaxq5m'


url = 'https://api.dune.com/api/v1/query/3334972/results?api_key=4mtutuc5rXoTQCzNnSZR87uvWQCdTbad'

result_response =  get(url)
data = pd.DataFrame(result_response.json()['result']['rows'])


df = data.copy()
df.dtypes
df = df.replace({float('nan'): None})

col_list = ['tick', 'tickLower', 'tickUpper']

df[col_list] = df[col_list].astype('Int64')




df.to_csv('uniswap_swap_WBTC_ETH_500_ETH_08-20-2024_09-01-2024.csv',index=False)



df

df.to_csv('uniswap_WBTC_WETH_100_liquidity_01-01-2020_09-01-2024.csv',index=False)




data.to_csv('uniswap_USDT_USDC_100_ETH_01-01-2020_08-20-2024.csv',index=False)
data.to_csv('USDT_USDC_contract_ARB 01-01-2020_06-15-2024.csv',index=False)
data.to_csv('USDT_USDC_contract_OP 01-01-2020_06-15-2024.csv',index=False)
data.to_csv('USDT_USDC_contract_Polygon 01-01-2020_06-15-2024.csv',index=False)
data.to_csv('USDT_USDC_contract_AVAX 01-01-2020_06-15-2024.csv',index=False)
data.to_csv('USDT_USDC_contract_BASE 01-01-2020_06-15-2024.csv',index=False)

data.to_csv('USDT-USDC 03-01-2023_03-15-2023 DEX.csv',index=False)


data.to_csv('data_DEX_trade_USDP_USDC_0409_0417.csv',index=False)
data.to_csv('data_DEX_trade_USDP_USDC_0409_0417.csv',index=False)
data.to_csv('data_DEX_trade_USDP_USDT_0409_0417.csv',index=False)


data.to_csv('data_DEX_trade_stETH_USDT_0322_0404.csv',index=False)

data.to_csv('data_DEX_trade_wstETH_WETH_1201_1203.csv',index=False)
data.to_csv('data_DEX_trade_OETH_WETH_0112_0119.csv',index=False)
data.to_csv('data_DEX_trade_crvUSD_USDC_0112_0119.csv',index=False)
data.to_csv('data_DEX_trade_crvUSD_USDC_0112_0119.csv',index=False)
data.to_csv('data_DEX_trade_MIM_USDC_0112_0119.csv',index=False)
data.to_csv('data_DEX_trade_LUSD_USDC_0112_0119.csv',index=False)

data.to_csv('data_DEX_trade_AVAX_USDC_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_AVAX_USDT_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_BTC_WETH_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_DOGE_WBNB_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_WETH_WBTC_0201_0207.csv',index=False)


data.to_csv('data_DEX_trade_WETH_USDC_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_WETH_DAI_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_WETH_USDT_0201_0207.csv',index=False)
data.to_csv('data_DEX_trade_WETH_WBTC_0201_0207.csv',index=False)

list_dex = list(data['project'])
print( list_dex )


###################################################
# Query Pagination
###################################################

import requests
import time 
url = "https://api.dune.com/api/v1/query/3334972/results"

headers = {"X-DUNE-API-KEY": "4mtutuc5rXoTQCzNnSZR87uvWQCdTbad"}

params = {"limit": 1, "offset": 0}  # Define limit and offset parameters

result_response = requests.request("GET", url, headers=headers, params=params)

print(response.text)

res_json = result_response.json()

offset_next = res_json['next_offset']
query_limit = 3
query_offset = 3
data = pd.DataFrame(res_json['result']['rows'])



data.to_csv('data_DEX_trade_WETH_USDC_0515_0531_test.csv',index=False)


import time 
def dune_data_download(file_path, query_id = 3334972, query_limit=1000,query_offset=0,
                       api_key = "4mtutuc5rXoTQCzNnSZR87uvWQCdTbad"):
    
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"
    headers = {"X-DUNE-API-KEY": api_key}
    
    # initial ingestion
    params = {"limit": 1, "offset": 0}
    result_response = requests.request("GET", url, headers=headers, params=params)    
    res_json = result_response.json()
    #print(res_json)   
    max_row_num = res_json['result']['metadata']['total_row_count']
    total_size_mb = res_json['result']['metadata']['total_result_set_bytes']/1024/1024
    offset_next = res_json['next_offset']
    #print(res_json)   
    print(f'max row number is: {max_row_num}')
    print(f'total size is: {total_size_mb:.2f} mb' )
    #print(res_json['datapoint_count'])
    #print(res_json)
    data = pd.DataFrame(res_json['result']['rows'])
    data.to_csv(file_path,  header=True, index=False)
    
    # download the data iteratively 
    while offset_next<=max_row_num:

        params = {"limit": query_limit, "offset": offset_next}
        result_response = requests.request("GET", url, headers=headers, params=params)    
        res_json = result_response.json()
        
        try:
            offset_next = res_json['next_offset']
            progressing_pct = offset_next/float(max_row_num)
            print(f'the current row is {offset_next}, completed {progressing_pct:.2%}') 
        
            data = pd.DataFrame(res_json['result']['rows'])
            data.to_csv(file_path, mode='a', header=False, index=False)
            
            time.sleep(2)
        except KeyError:
            print(f"the error occured: {KeyError}")
            offset_next = offset_next +query_limit
    
dune_data_download(file_path, query_id= 3334972, query_limit=5,query_offset=6164540)

file_path = 'data_DEX_trade_WETH_USDC_0515_0531.csv'
dune_data_download(file_path, query_id= 3334972, query_limit=30000,query_offset=0)


30000
###################################################
# Query Using the Dune python Clients
###################################################
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase

query = QueryBase(
    name="Sample Query",
    query_id=3325991,
    params=[
        #QueryParameter.text_type(name="TextField", value="Word"),
        #QueryParameter.number_type(name="NumberField", value=3.1415926535),
        QueryParameter.date_type(name="from_date", value="2024-01-04 00:00:00"),
        QueryParameter.date_type(name="to_date", value="2024-01-05 00:00:00"),
        #QueryParameter.enum_type(name="exchange", value=["balancer","sushiswap"]),
    ],
)
print("Results available at", query.url())
dotenv.load_dotenv(r'C:\Users\Hahn\Desktop\code\CL_DEX\analysis\dune_setting.env')
dune = DuneClient.from_env()

#results = dune.run_query(query)
results_df = dune.run_query_dataframe(query)
results_df['block_time']
results['results']
#%%
###################################################
# Query Using low level request functions
###################################################

API_KEY_DEX_AR_trade = '3GOU19aShwBovgC3hdt2AfqYXhRulu5h' # DEX_AR_trade
API_KEY_DS_TEAM = '4mtutuc5rXoTQCzNnSZR87uvWQCdTbad' #team


params = {
    "query_parameters": {    
        "from_date": "2022-01-04 00:00:00",
        "to_date": "2022-01-05 00:00:00",
        #"blockchain": "all"
        },

    "performance": "medium",
}
params = json.dumps(params)
#  Execute a Query
execution_id = execute_query("3325991",params, API_KEY_DS_TEAM)

response = get_query_status(execution_id, API_KEY_DS_TEAM)
response.json()
# Get Query Results
response = get_query_results(execution_id, API_KEY_DS_TEAM)
response.json()
data = pd.DataFrame(response.json()['result']['rows'])

data.to_csv('data_DEX_trade_wstETH_WETH.csv')


headers = {"X-Dune-API-Key": API_KEY_DS_TEAM}

query_id = 3325991
base_url = f"https://api.dune.com/api/v1/query/{query_id}/execute"
params = {
    "query_parameters": {    
        "from_date": "2024-01-04 00:00:00",
        "to_date": "2024-01-05 00:00:00",
        #"blockchain": "all"
        },

    "performance": "medium",
}
params_json = json.dumps(params)
result_response = post(base_url, headers=HEADER, params = params_json)
result_response.json()
result_response = requests.request("POST", base_url, headers=headers, json=params_json)

execution_id = result_response.json()['execution_id']



#%%
#################################
# utility functions
#################################

from requests import get, post
import requests
import pandas as pd
import json

BASE_URL = "https://api.dune.com/api/v1/"

def make_api_url(module, action, ID):
    """
    We shall use this function to generate a URL to call the API.
    """

    url = BASE_URL + module + "/" + ID + "/" + action
    print(url)
    return url
def execute_query(query_id, params, header):
    """
    Takes in the query ID and engine size.
    Specifying the engine size will change how quickly your query runs. 
    The default is "medium" which spends 10 credits, while "large" spends 20 credits.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    
    params = {
        "exchange": 'uniswap',
        "performance": engine,
    }
    """
    HEADER = {"x-dune-api-key" : header}
    url = make_api_url("query", "execute", query_id)
    response = requests.request("POST", url, headers=HEADER, params=params)
    #response = post(url, headers=HEADER, json = params)
    #execution_id = response.json()['execution_id']
    
    return response.json() #execution_id


def get_query_status(execution_id,header):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """
    HEADER = {"x-dune-api-key" : header}
    url = make_api_url("execution", "status", execution_id)
    response = get(url, headers=HEADER)

    return response


def get_query_results(execution_id, header):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """
    HEADER = {"x-dune-api-key" : header}
    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADER)

    return response


def cancel_query_execution(execution_id, header):
    """
    Takes in an execution ID.
    Cancels the ongoing execution of the query.
    Returns the response object.
    """
    HEADER = {"x-dune-api-key" : header}
    url = make_api_url("execution", "cancel", execution_id)
    response = get(url, headers=HEADER)
    
    return response
#%%