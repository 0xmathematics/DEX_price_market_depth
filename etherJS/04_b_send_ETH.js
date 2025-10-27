// Send ETH using the Wallet class
// Since playcode does not support the ethers.Wallet.createRandom() function, we can only run this code in VScode
import { ethers } from "ethers";

// Connect to the Ethereum test network using the Alchemy RPC node
// For how to prepare Alchemy API, please refer to https://github.com/AmazingAng/WTFSolidity/blob/main/Topics/Tools/TOOL04_Alchemy/readme.md
//const ALCHEMY_GOERLI_URL = 'https://eth-goerli.alchemyapi.io/v2/GlaeWuylnNM3uuOo-SAwJxuwTdqHaY5l';

//const ALCHEMY_GOERLI_URL = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
//const ALCHEMY_GOERLI_URL = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90' 
const infura_URL = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  
const provider = new ethers.JsonRpcProvider(infura_URL);





const privateKey = '0x9c30c88e284502c0dae5f313c6a50a63bea4f1d5c6bccdda0da72879f94eb1a2'
const wallet = new ethers.Wallet(privateKey, provider)
const mnemonic = wallet.mnemonic // Get the mnemonic phrase, not apply to polygon
const wallet_address = wallet.address
const wallet_address_receive = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'
console.log(`wallet address key is: ${wallet_address}\n`)
console.log(`wallet public key is: ${wallet.publicKey}\n`)
console.log(`wallet private key is: ${wallet.privateKey}\n`)
//console.log(`wallet mnemonic is: ${mnemonic.phrase}\n`)  //not apply to polygon



// 5. Send ETH
// If this wallet doesn't have any goerli testnet ETH, get some from a faucet, wallet address: 0xe16C1623c1AA7D919cd2241d8b36d9E79C1Be2A2
// 1. chainlink faucet: https://faucets.chain.link/goerli
// 2. paradigm faucet: https://faucet.paradigm.xyz/
console.log(`\n5. Send matic (polygon)`);
// i. Print balance before the transaction
console.log(`i. Balance before sending`)
console.log(`Wallet send: ${ethers.formatEther(await provider.getBalance(wallet_address))} matic`)
console.log(`Wallet receive: ${ethers.formatEther(await provider.getBalance(wallet_address_receive))} matic`)



// ii. Create transaction request, parameters: to is the receiving address, value is the amount of ETH
const tx = {
    to: wallet_address_receive,
    value: ethers.parseEther("8")
}

// iii. Send transaction and get receipt
console.log(`\nii. Waiting for transaction to be confirmed on the blockchain (may take a few minutes)`)
const receipt = await wallet.sendTransaction(tx)
await receipt.wait() // Wait for the transaction to be confirmed on the chain
console.log(receipt) // Print transaction details


// iv. Print balance after the transaction
console.log(`\niii. Balance after sending`)
console.log(`Wallet 1: ${ethers.formatEther(await provider.getBalance(wallet_address))} matic`)
console.log(`Wallet 2: ${ethers.formatEther(await provider.getBalance(wallet_address_receive))} matic`)

/*  */