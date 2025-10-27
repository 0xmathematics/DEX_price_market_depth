
import dotenv from 'dotenv';
dotenv.config();




import { fetchMaybeWhirlpool }  from "@orca-so/whirlpools-client";
import { createSolanaRpc, address, ClusterUrl } from '@solana/web3.js';
import { fetchAllMint } from "@solana-program/token";
import { sqrtPriceToPrice } from "@orca-so/whirlpools-core";


async function orca_state_price(solana_rpc_url: ClusterUrl, pool_string: string): number {
  //await setWhirlpoolsConfig('solanaDevnet');
  const solana_RPC = createSolanaRpc( solana_rpc_url );
  const pool_address = address(pool_string);
  const poolAccount = await fetchMaybeWhirlpool(solana_RPC, pool_address)
  

  if (poolAccount.exists) {
    console.log( poolAccount.data.sqrtPrice )

    let tokenA =  poolAccount.data.tokenMintA
    let tokenB =  poolAccount.data.tokenMintB
    const [mintA, mintB] = await fetchAllMint(solana_RPC, [tokenA, tokenB]);

    const poolPrice = sqrtPriceToPrice(
      poolAccount.data.sqrtPrice,
      mintA.data.decimals,
      mintB.data.decimals,
    );
    return poolPrice
    }
  else{
    console.log('no data returned')
    return 0
  }


}

const solana_rpc_url = process.env.SOLANA_RPC as ClusterUrl


// BONK/SOL "3ne4mWqdYuNiYrYZC9TrA3FcfuFdErghH97vNPbjicr1"  
// WBTC/SOL "B5EwJVDuAauzUEEdwvbuXzbFFgEYnUqqS37TUM1c4PQA"  
// cbBTC/SOL CeaZcxBNLpJWtxzt58qQmfMBtJY8pQLvursXTJYGQpbN
// WIF/SOL D6NdKrKNQPmRZCCnG1GqXtF7MMoHB7qR6GU5TkG59Qz1

//Bonk/SOL
let pool_string: string = "3ne4mWqdYuNiYrYZC9TrA3FcfuFdErghH97vNPbjicr1"  
let state_price:number = await orca_state_price(solana_rpc_url, pool_string)
console.log('BONK/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 


//WBTC/SOL
pool_string = "B5EwJVDuAauzUEEdwvbuXzbFFgEYnUqqS37TUM1c4PQA"  
state_price = await orca_state_price(solana_rpc_url, pool_string)
console.log('WBTC/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 

//cbBTC/SOL
pool_string = "CeaZcxBNLpJWtxzt58qQmfMBtJY8pQLvursXTJYGQpbN"  
state_price = await orca_state_price(solana_rpc_url, pool_string)
console.log('cbBTC/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 


//WIF/SOL
pool_string = "D6NdKrKNQPmRZCCnG1GqXtF7MMoHB7qR6GU5TkG59Qz1"  
state_price = await orca_state_price(solana_rpc_url, pool_string)
console.log('WIF/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 


//GOAT/SOL
pool_string = "4kKFykZkVqE5wbBgj6o8ddnj5TmA6UQgXJLYzAasgKdD"  
state_price = await orca_state_price(solana_rpc_url, pool_string)
console.log('GOAT/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 
