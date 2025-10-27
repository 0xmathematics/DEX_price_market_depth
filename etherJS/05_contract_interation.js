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

// Wmatic Contract: https://polygonscan.com/token/0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270#writeContract
const addressWmatic = '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270' 
const abiWmatic = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]';


const privateKey = '0x9c30c88e284502c0dae5f313c6a50a63bea4f1d5c6bccdda0da72879f94eb1a2'
const wallet = new ethers.Wallet(privateKey, provider)

// The rule for declaring a writable Contract variable is as follows:
// const contract = new ethers.Contract(address, abi, signer)
const contractWmatic = new ethers.Contract(addressWmatic, abiWmatic, wallet)

//convert a readable contract into a writable contract using the following method:
// const contract2 = contract.connect(signer)

// info for signer wallet 
const wallet_address = wallet.address
const wallet_address_receive = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'
console.log(`wallet address key is: ${wallet_address}\n`)
console.log(`wallet private key is: ${wallet.privateKey}\n`)
console.log(`Wallet matic balance: ${ethers.formatEther(await provider.getBalance(wallet_address))} matic`)


// 1. Read the singer wallet's Wmatic balance. 
// 1.  Read on-chain information of the Wmatic contract 
console.log("\n1. Read WETH balance")
const balanceWmatic = await contractWmatic.balanceOf(wallet_address)
console.log(`Wmatic balance before deposit: ${ethers.formatEther(balanceWmatic)}\n`)


// 2. Call the deposit() function of the WETH contract to convert 0.001 ETH into 0.001 WETH. Print the transaction details and the balance. 
console.log("\n2. Call the deposit() function to deposit 0.001 ETH")
// Send the transaction

/*
// Send a transaction
const tx = await contract.METHOD_NAME(args [, overrides])
// Wait for the transaction to be confirmed on the chain
await tx.wait()

[, overrides] is optional data that can be passed, including:

gasPrice: Gas price
gasLimit: Gas limit
value: Ether sent during the call (in wei)
nonce: Nonce

*/

const tx = await contractWmatic.deposit({value: ethers.parseEther("0.001")})
// Wait for the transaction to be confirmed
await tx.wait()
console.log(`Transaction details:`)
console.log(tx)
const balanceWmatic_deposit = await contractWmatic.balanceOf(wallet_address)
console.log(`Wmatic balance after deposit: ${ethers.formatEther(balanceWmatic_deposit)}\n`)

// 3. transfer()

console.log("\n3. Call the transfer() function to transfer 0.001 WETH to another wallet")
// Send the transaction
const tx2 = await contractWmatic.transfer(wallet_address_receive, ethers.parseEther("0.001"))
// Wait for the transaction to be confirmed
await tx2.wait()
const balanceWETH_transfer = await contractWmatic.balanceOf(wallet_address)
console.log(`Wmatic balance after transfer: ${ethers.formatEther(balanceWETH_transfer)}\n`)





/* 
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

 */