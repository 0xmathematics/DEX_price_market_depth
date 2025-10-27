
// when es2022 is set in tsconfig.json, we can use top-level await
// import from other files needs to be ended with .js even if the file is .ts
import { uni_v3_pool_abi, erc20_abi  } from './pool_abi.js'; 
import {  ethers, parseUnits } from 'ethers';
import { BigNumber } from '@ethersproject/bignumber';
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

type TokenAmount = {
  x: number;
  y: number;
};

// Constants
const Q96 = 2n ** 96n;
const ONE_POINT_0001 = 1.0001;

/**
 * Computes square root of a number
 */
function sqrt(value: number): number {
  return Math.sqrt(value);
}

/**
 * Convert BigInt to float from Q96 fixed-point format
 */
function fromQ96(sqrtPriceX96: bigint): number {
  return Number(sqrtPriceX96) / Number(Q96);
}

export function getTokenAmount(
  tickCurrent: number,
  tickLower: number,
  tickUpper: number,
  liquidity: bigint,
  sqrtPriceX96: bigint
): TokenAmount {
  const sqrtPl = sqrt(Math.pow(ONE_POINT_0001, tickLower));
  const sqrtPu = sqrt(Math.pow(ONE_POINT_0001, tickUpper));
  const sqrtP = fromQ96(sqrtPriceX96);

  let x = 0;
  let y = 0;

  const liquidityFloat = Number(liquidity); // assume liquidity fits into JS number

  if (tickCurrent <= tickLower) {
    x = liquidityFloat * (sqrtPu - sqrtPl) / (sqrtPl * sqrtPu);
    y = 0;
  } else if (tickCurrent < tickUpper) {
    x = liquidityFloat * (sqrtPu - sqrtP) / (sqrtP * sqrtPu);
    y = liquidityFloat * (sqrtP - sqrtPl);
  } else {
    x = 0;
    y = liquidityFloat * (sqrtPu - sqrtPl);
  }

  return { x, y };
}

async function getTokenDetails(tokenContract: ethers.Contract): Promise<{ name: string; symbol: string; decimals: number }> {
  const [name, symbol, decimals] = await Promise.all([
    tokenContract.name(),
    tokenContract.symbol(),
    tokenContract.decimals(),
  ]);
  return { name, symbol, decimals };
}



const infura_url = "https://optimism-mainnet.infura.io/v3/52757b6af51f4a50a7645433e21e0d90" 
const provider = new ethers.JsonRpcProvider(infura_url);

const USDC = new Token(1, '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 6, 'USDC', 'USD Coin');
const WETH = new Token(1, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 18, 'WETH', 'Wrapped Ether');

const fee = FeeAmount.MEDIUM; // 0.3% = 3000
/** 
const poolAddress = computePoolAddress({
factoryAddress: '0x1F98431c8aD98523631AE4a59f267346ea31F984', // Uniswap V3 factory
tokenA: USDC,
tokenB: WETH,
fee,
});

*/
// const pool_address = '0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8'; // USDC/WETH pool address on mainnet
const pool_address = '0xaDAb76dD2dcA7aE080A796F0ce86170e482AfB4a'; // USDC/WBTC pool address on optimism

const poolContract = new ethers.Contract(pool_address, uni_v3_pool_abi, provider);

let [slot0, liquidity, tick_spacing,token_address_0, token_address_1] = await Promise.all([
poolContract.slot0(),
poolContract.liquidity(),
poolContract.tickSpacing(),
poolContract.token0(),
poolContract.token1(),
]);

console.log("slot0 is: ", slot0) 
console.log("liquidity is: ",liquidity) 
console.log("tickspacing is: ",tick_spacing)
console.log(token_address_0)
console.log(token_address_1)


/*
// Get token details
// token_address_0 and token_address_1 are the addresses of the tokens in the pool
const token_0_contract = new ethers.Contract(token_address_0, erc20_abi, provider);
const token_1_contract = new ethers.Contract(token_address_1, erc20_abi, provider);
const [token_0_info, token_1_info] = await Promise.all([getTokenDetails(token_0_contract), getTokenDetails(token_1_contract)]);

console.log("token_0_info decimal: ", token_0_info.decimals);
console.log("token_0_info: ", token_1_info);

*/



const current_tick = slot0[1];
console.log("current_tick is: ", current_tick);
const sqrt_price_x96 = slot0[0];
console.log("sqrt_price_x96 is: ", sqrt_price_x96);

const lower_tick = current_tick - 200n;  
const upper_tick = current_tick + 200n; 

const { x, y } = getTokenAmount(
  Number(current_tick),
  Number(lower_tick),
  Number(upper_tick),
  liquidity,
  sqrt_price_x96
);
console.log("x is: ", x);
console.log("y is: ", y);



console.log("lower_tick is: ", lower_tick);
console.log("upper_tick is: ", upper_tick);
const checksummedAddress = ethers.getAddress('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48')  // all lowercase is fine here
console.log(checksummedAddress)  // → returns correct checksummed version
console.log("checksummedAddress aaaaaa")  // → returns correct checksummed version



