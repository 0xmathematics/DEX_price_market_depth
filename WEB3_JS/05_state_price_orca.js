
// author: Hang Miao
// date: Dec 12th, 2024

import "dotenv/config";
//console.log(process.env.SOLANA_RPC);
dotenv.config();

import { Connection, PublicKey,LAMPORTS_PER_SOL } from "@solana/web3.js";

import { BN } from "bn.js"

console.log(process.env.SOLANA_RPC)

/** 
// replacing the process.env.SOLANA_RPC by custom PRC: "https: ..."
//const connection = new Connection(process.env.SOLANA_RPC, "confirmed");  //"recent" "confirmed"

// input the pool address or pool id
//const pool_ID_GOAT_SOL = "44YBnjSTkGxhPW8ZpYBFpfGb1tNP6Epzi83SpF2WcbnL"
//const pool_ID_JUP_SOL = 'EZVkeboWeXygtq8LMyENHyXdF5wpYrtExRNH9UwB1qYw'
//const pool_ID_WIF_SOL = 'BuavWdfsNTfmEQbnPt2PLc51B7pifRNhqNiDUtGLeNNn'
//const pool_ID_BONK_SOL = 'BjZKz1z4UMjJPvPfKwTwjPErVBWnewnJFvcZB6minymy'
const pool_ID_WBTC_SOL = 'B5EwJVDuAauzUEEdwvbuXzbFFgEYnUqqS37TUM1c4PQA'

// print public address 
console.log(pool_ID_WBTC_SOL)

*/



/** 
async function state_price_raydium_clmm(connection, address_pool_ID) {

  const address_pub_key = new PublicKey(address_pool_ID)
  const info = await connection.getAccountInfo(address_pub_key);
  if (!info) return;
  
  // Assuming the structure was successfully decoded
  const account_data = PoolInfoLayout.decode(info.data);
  
  const sqrt_price = account_data.sqrtPriceX64

  const decimal_0 = account_data.mintDecimalsA
  const decimal_1 = account_data.mintDecimalsB

  //const state_price = (sqrt_price**2/2**128)*10**(decimal_0-decimal_1)
  const state_price = SqrtPriceMath.sqrtPriceX64ToPrice(sqrt_price, decimal_0, decimal_1)
  
  //const state_price = sqrt_price



  return state_price
}

*/





/**
let state_price = await state_price_raydium_clmm(connection, pool_ID_GOAT_SOL)

// we have the state price as follows, we need to pick up the one the suits the appropriate base/quote order
console.log(state_price)
console.log(1/state_price)

 */

/**
// state price for 

// pool_ID_RAY_SOL pool_ID_SPX_SOL
let state_price = await state_price_raydium_clmm(connection, pool_ID_SPX_SOL)



console.log(state_price)
console.log(1/state_price)


*/