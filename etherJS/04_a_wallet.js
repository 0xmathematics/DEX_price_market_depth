// Send ETH using the Wallet class
// Since playcode does not support the ethers.Wallet.createRandom() function, we can only run this code in VScode
import { ethers } from "ethers";

// Connect to the Ethereum test network using the Alchemy RPC node
// For how to prepare Alchemy API, please refer to https://github.com/AmazingAng/WTFSolidity/blob/main/Topics/Tools/TOOL04_Alchemy/readme.md
//const ALCHEMY_GOERLI_URL = 'https://eth-goerli.alchemyapi.io/v2/GlaeWuylnNM3uuOo-SAwJxuwTdqHaY5l';

//const ALCHEMY_GOERLI_URL = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
//const ALCHEMY_GOERLI_URL = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90' 
const ALCHEMY_GOERLI_URL = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  
const provider = new ethers.JsonRpcProvider(ALCHEMY_GOERLI_URL);


// Create a wallet object with a random private key
const wallet1 = ethers.Wallet.createRandom()
const wallet1WithProvider = wallet1.connect(provider)
const mnemonic = wallet1.mnemonic // Get the mnemonic phrase

console.log(`wallet address key is: ${wallet1.address}\n`)
console.log(`wallet public key is: ${wallet1.publicKey}\n`)
console.log(`wallet private key is: ${wallet1.privateKey}\n`)
console.log(`wallet mnemonic is: ${mnemonic.phrase}\n`)

/* */
const privateKey = '0x227dbb8586117d55284e26620bc76534dfbd2394be34cf4a09cb775d593b6f2b'
const wallet2 = new ethers.Wallet(privateKey, provider)

console.log(`wallet2 address key is: ${wallet2.address}\n`)
console.log(`Wallet2 private key: ${wallet2.privateKey}`)


const wallet3 = ethers.Wallet.fromPhrase(mnemonic.phrase)


const address1 = await wallet1.getAddress()
const address2 = await wallet2.getAddress() 
const address3 = await wallet3.getAddress() // Get the addresses
console.log(`1. Get the wallet addresses`);
console.log(`Address of Wallet 1: ${address1}`);
console.log(`Address of Wallet 2: ${address2}`);
console.log(`Address of Wallet 3: ${address3}`);
console.log(`Are the addresses of Wallet 1 and Wallet 3 the same? ${address1 === address3}`);


// 5. Get Private Key
const txCount1 = await provider.getTransactionCount(wallet1WithProvider)
const txCount2 = await provider.getTransactionCount(wallet2)
console.log(`Number of transactions sent by Wallet 1: ${txCount1}`)
console.log(`Number of transactions sent by Wallet 2: ${txCount2}`)

/*
//    

 */

