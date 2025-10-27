import dotenv from 'dotenv';
dotenv.config();

//import "dotenv/config";
console.log(process.env.SOLANA_RPC);
const RPC_LINK: string = process.env.SOLANA_RPC as string
const connection = new Connection(RPC_LINK, "confirmed");  //"recent" "confirmed"



import { Connection, PublicKey,LAMPORTS_PER_SOL } from "@solana/web3.js";
import { fetchSplashPool, setWhirlpoolsConfig } from '@orca-so/whirlpools';
import { OrcaWhirlpoolClient } from "@orca-so/whirlpool-sdk";

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