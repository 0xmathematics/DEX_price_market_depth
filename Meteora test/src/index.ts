
import DLMM from '@meteora-ag/dlmm'
import dotenv from 'dotenv';
import {
    Connection,
    PublicKey,
    clusterApiUrl,
    LAMPORTS_PER_SOL,
  } from "@solana/web3.js";
import { getMint } from "@solana/spl-token";

import AmmImpl, { MAINNET_POOL } from '@mercurial-finance/dynamic-amm-sdk';
import { Wallet, AnchorProvider } from '@project-serum/anchor';
//import {createProgram} from '@mercurial-finance/dynamic-amm-sdk/'
import {BN} from 'bn.js';

dotenv.config();

const solana_rpc_url = process.env.SOLANA_RPC

//const address = new PublicKey("HQCtRaHWyfqGcS7gFmvAn2vVgG7ZT2PQjBdsPd4RGNZy");  //
//const address = new PublicKey("5rCf1DM8LjKTw4YqhnoLcngyZYeNnQqztScTogYHAS6");  //

//const address = new PublicKey("9t1H1uDJ558iMPNkEPSN1fqkpC4XSPQ6cqSf6uEsTfTR");



async function meteora_DLMM_state_price(solana_rpc_url: string, pool_string: string): Promise<number> {
  //await setWhirlpoolsConfig('solanaDevnet');
  const connection = new Connection(solana_rpc_url as string,"confirmed");


  console.log( connection )
  const address = new PublicKey(pool_string);  //
  //const dlmmObject =  new DLMM()
  const dlmm = ((DLMM)as any).default;
  const dlmmPool = await dlmm.create(connection, address);
    
  /** */
  const activeBin = await dlmmPool.getActiveBin();

  const activeBinPriceLamport = activeBin.price;

  const decimal_token0 = dlmmPool.tokenX.decimal
  const decimal_token1 = dlmmPool.tokenY.decimal
  const poolPrice = activeBinPriceLamport * 10**(decimal_token0-decimal_token1)

//console.log( activeBinPriceLamport)


  if (poolPrice) {
    return poolPrice
    }
  else{
    console.log('no data returned')
    return 0
  }


}


async function meteora_DAMM_state_price(solana_rpc_url: string, pool_string: string): Promise<number> {
  //await setWhirlpoolsConfig('solanaDevnet');
  const connection = new Connection(solana_rpc_url as string,"confirmed");


  console.log( connection )
  const address = new PublicKey(pool_string);  //
  //const dlmmObject =  new DLMM()
  const dlmm = ((DLMM)as any).default;
  const dlmmPool = await dlmm.create(connection, address);
    
  /** */
  const activeBin = await dlmmPool.getActiveBin();

  const activeBinPriceLamport = activeBin.price;

  const decimal_token0 = dlmmPool.tokenX.decimal
  const decimal_token1 = dlmmPool.tokenY.decimal
  const poolPrice = activeBinPriceLamport * 10**(decimal_token0-decimal_token1)

//console.log( activeBinPriceLamport)


  if (poolPrice) {
    return poolPrice
    }
  else{
    console.log('no data returned')
    return 0
  }


}


/** 
const connection = new Connection(solana_rpc_url as string,"confirmed");

const address = new PublicKey("32D4zRxNc1EssbJieVHfPhZM3rH6CzfUPrWUuWxD9prG"); 

const ammimpl_ = ((AmmImpl)as any).default;
const stablePool = await ammimpl_.create(connection, address);

//const stablePool = await AmmImpl.create(connection, address);

//const constantProductPool = await AmmImpl.create(connection, MAINNET_POOL.USDC_SOL);
//const stablePool = await AmmImpl.create(connection, MAINNET_POOL.USDT_USDC);
const USDT_USDC_pool = new PublicKey(MAINNET_POOL.USDC_SOL)
console.log( USDT_USDC_pool)

*/

async function meteora_stable_state_price(solana_rpc_url: string, pool_string: string): Promise<number> {
  //await setWhirlpoolsConfig('solanaDevnet');
  const connection = new Connection(solana_rpc_url as string,"confirmed");


  console.log( connection )
  const address = new PublicKey(pool_string);  //
  //const dlmmObject =  new DLMM()
  const ammimpl_ = ((AmmImpl)as any).default;
  const stablePool = await ammimpl_.create(connection, address);
    
  // Get the decimal for token reserves
  const tokenA_address = stablePool.poolState.tokenAMint
  const tokenB_address = stablePool.poolState.tokenBMint

  // Fetch the mint information for the token
  const mintInfo_A = await getMint(connection, tokenA_address);
  const decimals_A = mintInfo_A.decimals;

  const mintInfo_B = await getMint(connection, tokenB_address);
  const decimals_B = mintInfo_B.decimals;

  const delta_amount = 0.001
  // A -> B
  let inTokenMint = tokenA_address
  let inAmountLamport = new BN(delta_amount * 10 ** decimals_A);

  let bbb = await stablePool.getSwapQuote(inTokenMint, inAmountLamport)

  let swapOutAmount_B = bbb.swapOutAmount
  const price_A_B = parseFloat(swapOutAmount_B.toString(10))* 10 **(-decimals_B) / delta_amount;
  console.log( price_A_B )


  // B -> A
  inTokenMint = tokenB_address
  inAmountLamport = new BN(delta_amount * 10 ** decimals_B);

  let aaa = await stablePool.getSwapQuote(inTokenMint, inAmountLamport)
  let swapOutAmount_A = aaa.swapOutAmount
  const price_B_A = parseFloat(swapOutAmount_A.toString(10))* 10 **(-decimals_A) / delta_amount;
  console.log( price_B_A )


 // if a base; b quote. Price A/B 
 return (price_A_B + 1/price_B_A)/2
}



//PENGU/USDC
let pool_string: string = "5rCf1DM8LjKTw4YqhnoLcngyZYeNnQqztScTogYHAS6"  
let state_price:number = await meteora_DLMM_state_price(solana_rpc_url as string, pool_string)
console.log('PENGU/USDC state price is: '); 
console.log(state_price); 
console.log(1/state_price); 

//Fartcoin/SOL
pool_string = "6wJ7W3oHj7ex6MVFp2o26NSof3aey7U8Brs8E371WCXA"  
state_price = await meteora_DLMM_state_price(solana_rpc_url as string, pool_string)
console.log('Fartcoin/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 

//JLP/USDC
pool_string = "DbTk2SNKWxu9TJbPzmK9HcQCAmraBCFb5VMo8Svwh34z"  
state_price = await meteora_DLMM_state_price(solana_rpc_url as string, pool_string)
console.log('JLP/USDC state price is: '); 
console.log(state_price); 
console.log(1/state_price); 


//SWARMS/SOL
pool_string = "4ahjvr2TN7yViD8b54S1TCC2CokRfSBYErYT3Zd7rK9u"  
state_price = await meteora_DLMM_state_price(solana_rpc_url as string, pool_string)
console.log('SWARMS/SOL state price is: '); 
console.log(state_price); 
console.log(1/state_price); 




//USDC/USDT
pool_string = "32D4zRxNc1EssbJieVHfPhZM3rH6CzfUPrWUuWxD9prG"  
state_price = await meteora_stable_state_price(solana_rpc_url as string, pool_string)
console.log('USDC/USDT state price is: '); 
console.log(state_price); 
console.log(1/state_price);




/**


const pool_Vault_LP_A = stablePool.accountsInfo.poolVaultALp
const pool_Vault_LP_B = stablePool.accountsInfo.poolVaultBLp
const pool_Vault_state_A = stablePool.vaultA.vaultState
const pool_Vault_state_B = stablePool.vaultB.vaultState
const pool_Vault_LP_supply_A = stablePool.accountsInfo.vaultALpSupply
const pool_Vault_LP_supply_B = stablePool.accountsInfo.vaultBLpSupply
const pool_Vault_reserve_A = stablePool.accountsInfo.vaultAReserve
const pool_Vault_reserve_B = stablePool.accountsInfo.vaultBReserve

console.log(pool_Vault_LP_A.toString(10))
//console.log(pool_Vault_LP_B.toString(10))
console.log(pool_Vault_state_A)
console.log(pool_Vault_LP_supply_A.toString(10))
console.log(pool_Vault_reserve_A.toString(10))

 */




/*
const { poolTokenAmountOut, tokenAInAmount, tokenBInAmount } = stablePool.getDepositQuote(
  inAmountALamport,
  inAmountBLamport,
  false, // pass in false for imbalance deposit quote
); // Web3 Transaction Object
const depositTx = await stablePool.deposit(mockWallet.publicKey, tokenAInAmount, tokenBInAmount, poolTokenAmountOut);
const depositResult = await provider.sendAndConfirm(depositTx); // Transaction hash

*/







//const stablePool = await AmmImpl.create(connection, MAINNET_POOL.USDC_SOL);

// SOL/USDC "5rCf1DM8LjKTw4YqhnoLcngyZYeNnQqztScTogYHAS6"  
// PENGU/USDC "HQCtRaHWyfqGcS7gFmvAn2vVgG7ZT2PQjBdsPd4RGNZy"  
// JLP/USDC DbTk2SNKWxu9TJbPzmK9HcQCAmraBCFb5VMo8Svwh34z
// WIF/SOL D6NdKrKNQPmRZCCnG1GqXtF7MMoHB7qR6GU5TkG59Qz1




/** 
//SOL/USDC
let pool_string: string = "5rCf1DM8LjKTw4YqhnoLcngyZYeNnQqztScTogYHAS6"  
let state_price:number = await meteora_DLMM_state_price(solana_rpc_url as string, pool_string)
console.log('SOL/USDC state price is: '); 
console.log(state_price); 
console.log(1/state_price); 


//USDC/USDT
let pool_string = "32D4zRxNc1EssbJieVHfPhZM3rH6CzfUPrWUuWxD9prG"  
let state_price = await meteora_stable_state_price(solana_rpc_url as string, pool_string)
console.log('USDC/USDT state price is: '); 
console.log(state_price); 
console.log(1/state_price);
*/


