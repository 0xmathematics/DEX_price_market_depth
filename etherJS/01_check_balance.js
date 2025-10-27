//console.log("Hello, World!");

import { ethers } from "ethers";
//const ALCHEMY_GOERLI_URL = 'https://polygon-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90'  
const infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 

const provider = new ethers.JsonRpcProvider(infura_url);

const main = async () => {
    const balance = await provider.getBalance(`vitalik.eth`);
    console.log(`ETH Balance of vitalik: ${ethers.formatEther(balance)} ETH`);
}
main()