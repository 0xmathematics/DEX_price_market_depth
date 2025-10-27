# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:04:12 2023

@author: Hang
"""











import os
#os.chdir(r'/Users/yeminlan/Dropbox/python/ts/wavelets')
os.chdir(r'C:\Users\Hahn\Desktop\code\python\web3\uniswap v3')
os.chdir(r'/Users/hang.miaosmartcontract.com/Documents/GitHub/DEX_Development_Kit/reference')
from math import cos,sin,pi,exp,log,log10,sqrt,ceil,floor
import uniswap_v3_math as uni


uni.example_1() 
# optimism WBTC/ETH 0.3%
# tx hash = 0x707bafa97e0b2c6ae78f3d77c3b21e8dce9a3abbe543f0b9d14346b301f51324
x = 9860944
y = 510623461790347930
dL = 95009144914601
ta = -262440
tb = -261540
d0 = 8
d1 = 18
pa = 1.0001**ta
pb = 1.0001**tb
pa = uni.tick_to_price(ta,d0,d1)
pb = uni.tick_to_price(tb,d0,d1)

P = y/x
L = sqrt(x*y)




# tx hash = 0x5c8fc568f8d7db8b92d3867af42a5c0d39e1951d40ed1cdc76fc173399ad4ce1
x = 9860944
y = 510623461790347930
dL = 95009144914601
ta = 256310
tb = 257390
d0 = 8
d1 = 18
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
