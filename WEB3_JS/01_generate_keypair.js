//console.log("Hello, World!");

import "dotenv/config";
//import dotenv from 'dotenv';
//dotenv.config();
console.log(process.env.SECRET_KEY);

import { Keypair } from "@solana/web3.js";
import { getKeypairFromEnvironment } from "@solana-developers/helpers";
import bs58 from 'bs58';


const keypair = getKeypairFromEnvironment("SECRET_KEY");
const privateKeyBase58 = bs58.encode(keypair.secretKey);

console.log(`✅ Generated keypair!`);
console.log(`The public key is: `, keypair.publicKey.toBase58());
console.log(`The secret key of form uint8array is: `, keypair.secretKey);
console.log(`The secret key of form base58 is: `, privateKeyBase58);
console.log(`✅ Finished!`);



/* 
const keypair = Keypair.generate();

console.log(`✅ Generated keypair!`);
console.log(`The public key is: `, keypair.publicKey.toBase58());
console.log(`The secret key is: `, keypair.secretKey);
console.log(`✅ Finished!`);


*/