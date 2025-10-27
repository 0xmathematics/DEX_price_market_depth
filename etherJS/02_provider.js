
import { ethers } from "ethers";

const infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
//const ALCHEMY_GOERLI_URL = 'https://eth-goerli.alchemyapi.io/v2/GlaeWuylnNM3uuOo-SAwJxuwTdqHaY5l';
// Connect to the Ethereum mainnet
const providerETH = new ethers.JsonRpcProvider(infura_url)

/* 

// 1. check with balance of one address
console.log("1. Retrieving the ETH balance of Vitalik on the mainnet");
const balance = await providerETH.getBalance(`vitalik.eth`);
///const balanceGoerli = await providerGoerli.getBalance(`vitalik.eth`);
// Output the balances on the console (mainnet)
console.log(`ETH Balance of Vitalik: ${ethers.formatEther(balance)} ETH`);
// Output the Goerli testnet ETH balance
//console.log(`Goerli ETH Balance of Vitalik: ${ethers.formatEther(balanceGoerli)} ETH`);


// 2. Check which chain the provider is connected to
console.log("\n2. Checking which chain the provider is connected to")
const network = await providerETH.getNetwork();
console.log(network.toJSON());


// 3. Retrieve the current block number
console.log("\n3. Retrieving the current block number")
const blockNumber = await providerETH.getBlockNumber();
console.log(blockNumber);


// 4. Retrieve the transaction count of Vitalik's wallet
console.log("\n4. Retrieving the transaction count of Vitalik's wallet")
const txCount = await providerETH.getTransactionCount("vitalik.eth");
console.log(txCount);


// 5. Retrieve the current recommended gas settings
console.log("\n5. Retrieving the current recommended gas settings")
const feeData = await providerETH.getFeeData();
console.log(feeData);


// 6. Retrieve information about a specific block
console.log("\n6. Retrieving information about a specific block")
const block = await providerETH.getBlock(0);
console.log(block);
*/
// 7. Retrieve the bytecode of a contract at a specific address, using the contract address of WETH on the mainnet as an example
console.log("\n7. Retrieving the bytecode of a contract at a specific address, using the contract address of WETH on the mainnet as an example")
const code = await providerETH.getCode("0xc778417e063141139fce010982780140aa0cd5ab");
console.log(code);