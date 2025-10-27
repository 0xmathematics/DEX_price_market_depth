import {
    Connection,
    PublicKey,
    clusterApiUrl,
    LAMPORTS_PER_SOL,
  } from "@solana/web3.js";
   
  const connection = new Connection("https://solana-mainnet.g.alchemy.com/v2/3Rn8S1bDpHZXpqKMTAXDg6HbxFp5QOpm");
  const address = new PublicKey("AVs9TA4nWDzfPJE9gGVNJMVhcQy3V9PGazuz33BfG2RA");
  const balance = await connection.getBalance(address);
  const balanceInSol = balance / LAMPORTS_PER_SOL;
   
  console.log(`The balance of the account at ${address} is ${balanceInSol} SOL`);
  console.log(`✅ Finished!`);


/* 
const keypair = Keypair.generate();

console.log(`✅ Generated keypair!`);
console.log(`The public key is: `, keypair.publicKey.toBase58());
console.log(`The secret key is: `, keypair.secretKey);
console.log(`✅ Finished!`);


*/