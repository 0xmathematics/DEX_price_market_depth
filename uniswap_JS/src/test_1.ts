import { Token } from '@uniswap/sdk-core'
import { Pool } from '@uniswap/v3-sdk'
import { getAddress } from 'ethers'
import { TickMath } from '@uniswap/v3-sdk'
import JSBI from 'jsbi'
// ✅ Normalize address (safe for lowercase or user-provided input)
const normalize = (addr: string): string => {
  return getAddress(addr) // ethers@6 will throw if invalid
}

// USDC & DAI tokens on Ethereum mainnet
const USDC = new Token(
  1,
  //normalize('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'),
  '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
  6,
  'USDC',
  'USD Coin'
)

const DAI = new Token(
  1,
  normalize('0x6b175474e89094c44da98b954eedeac495271d0f'),
  18,
  'DAI',
  'Dai Stablecoin'
)
const sqrtPriceX96 = JSBI.BigInt(79228162514264337593543950336) // = 2^96
const tick = TickMath.getTickAtSqrtRatio(sqrtPriceX96) // ✅ get consistent tick

// ✅ Construct a mock pool (fake values for illustration)
const pool = new Pool(
  USDC,
  DAI,
  3000, // fee tier: 0.3%
  sqrtPriceX96, // sqrtPriceX96: 1.0 price ratio
  1000000, // liquidity
  tick // current tick
)

console.log('Pool Info:')
console.log('Token0:', pool.token0.symbol)
console.log('Token1:', pool.token1.symbol)
console.log('Fee:', pool.fee)
console.log('Price token0/token1:', pool.token0Price.toSignificant(6))
console.log('Price token1/token0:', pool.token1Price.toSignificant(6))