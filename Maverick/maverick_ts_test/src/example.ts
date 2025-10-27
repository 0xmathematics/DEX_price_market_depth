import dotenv from 'dotenv';
dotenv.config();

//import "dotenv/config";
console.log(process.env.infura_url_ethereum);
const RPC_LINK: string = process.env.infura_url_ethereum as string
import { maverickAbi } from './maverickV2Abi'
import { getERC20TokenInfo } from './utils/tokenInfo'
import { maverickPoolInfoAbi } from './maverickPoolInfoV2Abi'




import { ethers, Contract } from "ethers";
const provider = new ethers.JsonRpcProvider(RPC_LINK);
let contractAddress = '0x14cf6d2fe3e1b326114b07d22a6f6bb59e346c67'
// GHO/USDC
contractAddress = "0x14cf6d2fe3e1b326114b07d22a6f6bb59e346c67"

// MAV/ETH
contractAddress = "0x97a3eb00eb67e6e92d43dfe9c28f5211e05e2342"

// USDC/USDS
contractAddress = "0xdf9c440111a17eafbecf5db37dd04c948e878878"

// USDC/USDT
contractAddress = "0x31373595f40ea48a7aab6cbcb0d377c6066e2dca"




const poolInfoContractAddress  = "0x942646b0A8B42Af1e1044439013436a9a3e080b5"
const poolInfoContract = new Contract(poolInfoContractAddress, maverickPoolInfoAbi, provider)



const poolContract = new Contract(contractAddress, maverickAbi, provider)

function wait(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const main = async () => {


    const [baseTokenAddress, quoteTokenAddress] = await Promise.all([poolContract.tokenA(), poolContract.tokenB()])
    console.log(`base token address is: ${baseTokenAddress} `);
    console.log(`quote token address is: ${quoteTokenAddress} `);
    const [base, quote] = await getERC20TokenInfo([baseTokenAddress, quoteTokenAddress], provider)
    const decimals_0 = Number(base.decimal)
    const decimals_1 = Number(quote.decimal)
    console.log(`base token decimal is: ${decimals_0} `);
    console.log(`quote token decimal is: ${decimals_1} `);
   /**/
    await wait(1000)

    const scale0 =  Number(await poolContract.tokenAScale())
    const scale1 =  Number(await poolContract.tokenBScale())
    
    console.log(`base token scale is: ${scale0} `);
    console.log(`quote token scale is: ${scale1} `);

    const price = await poolInfoContract.getPoolPrice(contractAddress)
    const statePrice = 1 / (Number(price)*1/Math.sqrt(10**decimals_0*scale0*10**decimals_1*scale1)  )
    console.log(`state price is: ${statePrice} `);
    console.log(`state price is: ${1/statePrice} `);
    /**



    const [base, quote] = await getERC20TokenInfo([baseTokenAddress, quoteTokenAddress], provider)
    console.log(`base token address is: ${base} `);
    console.log(`quote token address is: ${quote} `);

     */
}
main()

/*
import { ethers } from "ethers";
  // Derive the Whirlpool address from token mints
const orca = new OrcaWhirlpoolClient({ connection });




const token0_address = new PublicKey("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"); // bonk
const token1_address = new PublicKey("So11111111111111111111111111111111111111112"); // sol
//const address = new PublicKey("9t1H1uDJ558iMPNkEPSN1fqkpC4XSPQ6cqSf6uEsTfTR");

const poolInfo = await fetchSplashPool(
    Connection,
    token0_address,
    token1_address
  );


  if (poolInfo.initialized) {
    console.log("Pool is initialized:", poolInfo);
  } else {
    console.log("Pool is not initialized:", poolInfo);
  };

  /**
const balance = await connection.getBalance(address);
const balanceInSol = balance / LAMPORTS_PER_SOL;

console.log(`The balance of the account at ${address} is ${balanceInSol} SOL`);
console.log(`✅ Finished!`);



import { isPositionInRange } from "@orca-so/whirlpools-core";

const currentSqrtPrice = 7448043534253661173n;
const tickIndex1 = -18304;
const tickIndex2 = -17956;

const inRange = isPositionInRange(currentSqrtPrice, tickIndex1, tickIndex2);
console.log("Position in range:", inRange);
 */

/** 
import { isPositionInRange } from "@orca-so/whirlpools-core";
const connection = new Connection(process.env.SOLANA_RPC, "confirmed");  //"recent" "confirmed"
//import { Connection, PublicKey,LAMPORTS_PER_SOL } from "@solana/web3.js";

//import { BN } from "bn.js"
*/