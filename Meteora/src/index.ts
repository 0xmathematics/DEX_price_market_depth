

import dotenv from 'dotenv';
import {
    Connection,
    PublicKey,
    clusterApiUrl,
    LAMPORTS_PER_SOL,
  } from "@solana/web3.js";

dotenv.config();

const solana_rpc_url = process.env.SOLANA_RPC

console.log( solana_rpc_url )
const connection = new Connection(solana_rpc_url as string,"confirmed");


console.log( connection )

const address = new PublicKey("9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump");  //fartcoin
//const address = new PublicKey("9t1H1uDJ558iMPNkEPSN1fqkpC4XSPQ6cqSf6uEsTfTR");



  
const info = await connection.getAccountInfo(address);

console.log( info.data )


/** const balance = await connection.getBalance(address);
const balanceInSol = balance / LAMPORTS_PER_SOL;

console.log( balanceInSol )
 * 
 * 
 * 
 * 
 * 





*/



/*

import { Chicken } from "./chicken";

console.log('hello hahaha' );

console.log('hello xixixi' );

console.log('hello hehehehe' );

console.log('hello bbbb' );

const chicken = new Chicken();

chicken.cluck();

 */