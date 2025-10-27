import { Provider, Contract, decodeBytes32String } from 'ethers'
import { erc20Abi } from './erc20Abi'

export type TokenInfo = {
  tokenAddress: string
  decimal: number
  symbol: string
}

const tokenInfoCache: { [key: string]: { tokenAddress: string; decimal: number; symbol: string } } = {}

export async function getERC20TokenInfo(tokenAddresses: string[], rpcProvider: Provider): Promise<TokenInfo[]> {
  return await Promise.all(
    tokenAddresses.map(async (tokenAddress) => {
      if (tokenInfoCache[tokenAddress]) {
        return tokenInfoCache[tokenAddress]
      }
      const erc20Contract = new Contract(tokenAddress, erc20Abi, rpcProvider)
      const decimal = await erc20Contract.decimals()
      let symbol: string
      try {
        symbol = await erc20Contract.symbol()
      } catch (e) {
        const erc20AbiPatched = erc20Abi.map((abi) => {
          if (abi.name === 'symbol') {
            return { ...abi, outputs: [{ name: '', type: 'bytes32' }] }
          }
          return abi
        })
        const erc20ContractPatched = new Contract(tokenAddress, erc20AbiPatched, rpcProvider)
        const symbolBytes = await erc20ContractPatched.symbol()
        symbol = decodeBytes32String(symbolBytes)
      }
      tokenInfoCache[tokenAddress] = { tokenAddress, decimal, symbol }

      return { tokenAddress, decimal, symbol }
    }),
  )
}
