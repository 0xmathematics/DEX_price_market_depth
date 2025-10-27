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
brew install websocat    # macOS
sudo apt install websocat  # Debian/Ubuntu

websocat -t wss://api.hyperliquid.xyz/ws
{"method":"subscribe","subscription":{"type":"l2Book","coin":"ETH", "coin":"ETH","nSigFigs": 3 }}    

'''
#%%

##################
# python state price
##################
import json
import websocket

def on_message(ws, message):
    data = json.loads(message)
    print(json.dumps(data, indent=2))

def on_open(ws):
    sub_msg = {
        "method": "subscribe",
        "subscription": {
            "type": "allMids",
            
        }
    }
    ws.send(json.dumps(sub_msg))
    print("Subscribed to all mids")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


ws = websocket.WebSocketApp(
    "wss://api.hyperliquid.xyz/ws",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)
ws.run_forever()

#%%
##################
# python limit orderbook
##################
import json
import websocket

def on_message(ws, message):
    data = json.loads(message)
    print(json.dumps(data, indent=2))

def on_open(ws):
    sub_msg = {
        "method": "subscribe",
        "subscription": {
            "type": "l2Book",
            "coin": "ETH",
            "nSigFigs": 3,
            
        }
    }
    ws.send(json.dumps(sub_msg))
    print("Subscribed to l2Book for ETH")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


ws = websocket.WebSocketApp(
    "wss://api.hyperliquid.xyz/ws",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)
ws.run_forever()



