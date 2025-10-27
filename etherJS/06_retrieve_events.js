// Send ETH using the Wallet class
// Since playcode does not support the ethers.Wallet.createRandom() function, we can only run this code in VScode
import { ethers } from "ethers";

// Connect to the Ethereum test network using the Alchemy RPC node
// For how to prepare Alchemy API, please refer to https://github.com/AmazingAng/WTFSolidity/blob/main/Topics/Tools/TOOL04_Alchemy/readme.md
//const ALCHEMY_GOERLI_URL = 'https://eth-goerli.alchemyapi.io/v2/GlaeWuylnNM3uuOo-SAwJxuwTdqHaY5l';

const infura_URL_ETH = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
//const ALCHEMY_GOERLI_URL = 'https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90' 
const infura_URL_polygon = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  
const provider_eth = new ethers.JsonRpcProvider(infura_URL_ETH);
const provider_polygon = new ethers.JsonRpcProvider(infura_URL_polygon);


// Wmatic Contract: https://polygonscan.com/token/0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270#writeContract
const addressWmatic = '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270' 
const abiWmatic = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]';

// weth Contract: https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
const contract_address = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2' 
const contract_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]';



// The rule for declaring a writable Contract variable is as follows:
// const contract = new ethers.Contract(address, abi, signer)
const contractWmatic = new ethers.Contract(addressWmatic, abiWmatic, provider_polygon)
const contractWETH = new ethers.Contract(contract_address, contract_abi, provider_eth)

/*
const privateKey = '0x9c30c88e284502c0dae5f313c6a50a63bea4f1d5c6bccdda0da72879f94eb1a2'
const wallet = new ethers.Wallet(privateKey, provider)



//convert a readable contract into a writable contract using the following method:
// const contract2 = contract.connect(signer)

// info for signer wallet 
const wallet_address = wallet.address
const wallet_address_receive = '0x666Ef6654B56885af2351c4C375519D7D8CC87a4'
console.log(`wallet address key is: ${wallet_address}\n`)
console.log(`wallet private key is: ${wallet.privateKey}\n`)
console.log(`Wallet matic balance: ${ethers.formatEther(await provider.getBalance(wallet_address))} matic`)

*/

// 1. Get the current block
const block_ETH = await provider_eth.getBlockNumber()
const block_Polygon = await provider_polygon.getBlockNumber()
console.log(`Current ETH block number: ${block_ETH}`);
console.log(`Current polygon block number: ${block_Polygon}`);
console.log(`Printing event details for ETH:`);  
const transferEvents = await contractWETH.queryFilter('Transfer', block_ETH - 10, block_ETH)
console.log(`Printing event details for polygon:`);  
const transferEvents_matic = await contractWmatic.queryFilter('Transfer', block_Polygon - 10, block_Polygon)
// Print the first Transfer event for ETH
console.log(transferEvents[0])

// Print the first Transfer event for Matic
console.log(transferEvents_matic[0])


// 2. Read the parsed results of the event.
// Parse the Transfer event data (variables are in args) for ETH
console.log("\n2. Parsing the event for ETH:");
const amount = ethers.formatUnits(ethers.getBigInt(transferEvents[0].args[2]), "ether");
console.log(`Address ${transferEvents[0].args[0]} transferred ${amount} WETH to address ${transferEvents[0].args[1]}`);


// Parse the Transfer event data (variables are in args) for Matic
console.log("\n2. Parsing the event for polygon:");
const amount_polygon = ethers.formatUnits(ethers.getBigInt(transferEvents_matic[0].args[2]), "ether");
console.log(`Address ${transferEvents_matic[0].args[0]} transferred ${amount_polygon} polygon to address ${transferEvents_matic[0].args[1]}`);


