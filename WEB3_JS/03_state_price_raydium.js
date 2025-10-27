
// author: Hang Miao
// date: Nov 27th, 2024

import "dotenv/config";
//console.log(process.env.SOLANA_RPC);

import { Connection, PublicKey,LAMPORTS_PER_SOL } from "@solana/web3.js";
import { LIQUIDITY_STATE_LAYOUT_V4 } from "@raydium-io/raydium-sdk";
import { BN } from "bn.js"



// replacing the process.env.SOLANA_RPC by custom PRC: "https: ..."
const connection = new Connection(process.env.SOLANA_RPC, "confirmed");  //"recent" "confirmed"

// input the pool address or pool id
const pool_ID_RAY_SOL = new PublicKey("AVs9TA4nWDzfPJE9gGVNJMVhcQy3V9PGazuz33BfG2RA");
const pool_ID_SPX_SOL = new PublicKey("9t1H1uDJ558iMPNkEPSN1fqkpC4XSPQ6cqSf6uEsTfTR");



async function state_price_raydium(connection, address_pool_ID) {

  
  const info = await connection.getAccountInfo(address_pool_ID);
  if (!info) return;
  
  // Assuming the structure was successfully decoded
  const account_data = LIQUIDITY_STATE_LAYOUT_V4.decode(info.data);


  const Vault_account_0 = account_data.baseVault //.toString()
  const Vault_account_1 = account_data.quoteVault // .toString()
  
  const vault_balance_0 = await connection.getTokenAccountBalance(Vault_account_0);
  const vault_balance_1 = await connection.getTokenAccountBalance(Vault_account_1);


  const decimal_0 = account_data.baseDecimal.toNumber()
  const decimal_1 = account_data.quoteDecimal.toNumber()


/**
  const PNL_need_0 = account_data.baseTotalPnl.toNumber()
  const PNL_need_1 = account_data.quoteTotalPnl.toNumber()

 */

const PNL_need_0 = account_data.baseNeedTakePnl.toNumber()
const PNL_need_1 = account_data.quoteNeedTakePnl.toNumber()
/*
const PNL_total_0 = account_data.baseTotalPnl.toNumber()
const PNL_total_1 = account_data.quoteTotalPnl.toNumber()
*/

let balance_0 = parseFloat( vault_balance_0.value.amount- PNL_need_0)/ 10**decimal_0
let balance_1 = parseFloat( vault_balance_1.value.amount- PNL_need_1 )/ 10**decimal_1 
const ratio_0 = balance_1/balance_0

/* 
   balance_0 = parseFloat( vault_balance_0.value.amount+ PNL_need_0)/ 10**decimal_0
   balance_1 = parseFloat( vault_balance_1.value.amount + PNL_need_1 )/ 10**decimal_1 
  const ratio_1 = balance_1/balance_0


  balance_0 = parseFloat( vault_balance_0.value.amount- PNL_total_0)/ 10**decimal_0
  balance_1 = parseFloat( vault_balance_1.value.amount- PNL_total_1 )/ 10**decimal_1 
  const ratio_2 = balance_1/balance_0

   balance_0 = parseFloat( vault_balance_0.value.amount+PNL_total_0)/ 10**decimal_0
   balance_1 = parseFloat( vault_balance_1.value.amount+ PNL_total_1 )/ 10**decimal_1 
  const ratio_3 = balance_1/balance_0

  console.log(1/ratio_0 )
  console.log(1/ratio_1 )
  console.log(1/ratio_2 )
  console.log(1/ratio_3 )
  console.log(PNL_need_0 )
  console.log(PNL_need_1 )
  //console.log(account_data.baseNeedTakePnl )
  //const ratio = vault_balance_1.value.uiAmount/vault_balance_0.value.uiAmount //* 10**decimal_0/10**decimal_1
*/


  return ratio_0
}

// state price for 

// pool_ID_RAY_SOL pool_ID_SPX_SOL
let state_price = await state_price_raydium(connection, pool_ID_SPX_SOL)



console.log(state_price)
console.log(1/state_price)


