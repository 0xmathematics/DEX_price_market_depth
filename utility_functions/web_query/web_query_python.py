#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:53:05 2025

@author: hang.miaosmartcontract.com
"""

import os
import requests
import browser_cookie3


# Extract Chrome cookies
cj = browser_cookie3.chrome(domain_name='.databricks.com')
from web3 import Web3
import numpy as np
import pandas as pd
import json
import datetime
import time
import tqdm
from math import sqrt, pi


os.chdir('/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/utility_functions/web_query')



#%%

####################################################
#  staleness
####################################################
df = pd.read_csv('Test_staleness_outage_state_price_market_depth.csv')
df
df_stale_2 = df[df['2-sec']>=0.1]
df_stale_15 = df[df['15-sec']>=0.1]
# create downloads folder
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

df.columns

urls_list = [  'https://2358092867114682.2.gcp.databricks.com/files/html_store_folder/EZETH_mobula-state_market_depth_15-sec_down.png?o=2358092867114682']
urls_list = df['url_link_15-sec'].tolist() + df['url_link_1-sec'].tolist()
for url in urls_list:
    filename = url.split("/")[-1].split("?")[0]  # Extracts file name from URL
    filepath = os.path.join(download_folder, filename)

    print(f"Downloading {filename}...")
    response = requests.get(url, cookies=cj, stream=True)
    
    if response.status_code == 200:
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Saved to {filepath}")
    else:
        print(f"Failed to download {url} - Status code: {response.status_code}")

print("All downloads completed.")


#%%

####################################################
#  Market Depth Overview
####################################################

df = pd.read_csv('UI_state_price_market_depth_pipeline.csv')
df

# create downloads folder
download_folder = "downloads_market_depth_overview"
os.makedirs(download_folder, exist_ok=True)

df.columns

# urls_list = [   'https://2358092867114682.2.gcp.databricks.com/files/html_store_folder/ZBTC_market_depth.html?o=2358092867114682']
urls_list = df['url_link'].tolist() 
for url in urls_list:
    filename = url.split("/")[-1].split("?")[0]  # Extracts file name from URL
    filepath = os.path.join(download_folder, filename)

    print(f"Downloading {filename}...")
    response = requests.get(url, cookies=cj, stream=True)
    
    if response.status_code == 200:
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Saved to {filepath}")
    else:
        print(f"Failed to download {url} - Status code: {response.status_code}")

print("All downloads completed.")