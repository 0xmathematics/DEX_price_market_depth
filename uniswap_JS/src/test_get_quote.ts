
import { uni_v3_pool_abi } from './pool_abi';
import { getAddress,ethers } from 'ethers'
import {
  Token,
  CurrencyAmount,
  TradeType,
} from '@uniswap/sdk-core';
import {
  Pool,
  Route,
  Trade,
  FeeAmount,
  computePoolAddress,
} from '@uniswap/v3-sdk';

const infura_url = "https://mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
const provider = new ethers.JsonRpcProvider(infura_url);

const USDC = new Token(1, '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 6, 'USDC', 'USD Coin');
const WETH = new Token(1, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 18, 'WETH', 'Wrapped Ether');

const fee = FeeAmount.MEDIUM; // 0.3% = 3000

const poolAddress = computePoolAddress({
factoryAddress: '0x1F98431c8aD98523631AE4a59f267346ea31F984', // Uniswap V3 factory
tokenA: USDC,
tokenB: WETH,
fee,
});

const poolContract = new ethers.Contract(poolAddress, uni_v3_pool_abi, provider);

async function aaaa() {
  const [slot0, liquidity] = await Promise.all([
    poolContract.slot0(),
    poolContract.liquidity(),
  ]);

  console.log(slot0, liquidity);
  return [slot0, liquidity];
}

/** 

let [slot0, liquidity] = await Promise.all([
poolContract.slot0(),
poolContract.liquidity(),
]);

console.log(poolAddress) 
console.log(slot0) 
console.log(liquidity) 

*/
// Example of using getAddress to normalize an address
const checksummedAddress = getAddress('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48')  // all lowercase is fine here
console.log(checksummedAddress)  // → returns correct checksummed version
