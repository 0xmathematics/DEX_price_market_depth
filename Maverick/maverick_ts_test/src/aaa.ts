import { CustomScript } from 'steps/customScript'
import { Contract } from 'ethers'
import { maverickPoolInfoAbi } from './maverickPoolInfoV2Abi'
import { maverickAbi } from './maverickV2Abi'
import { getERC20TokenInfo } from '../../utils/tokenInfo'
import { PoolPrice, evmLogsProcessor } from '../../utils/evmLogsProcessor'
import { getRpcProviderProxy, ProviderProxy } from '../../utils/rpc'

async function getPoolTokenRate(
  poolInfoContractAddress: string,
  contractAddress: string,
  blockNumber: number,
  rpcProviderProxy: ProviderProxy,
): Promise<PoolPrice[]> {
  const poolInfoContract = new Contract(poolInfoContractAddress, maverickPoolInfoAbi, rpcProviderProxy.provider)
  const poolContract = new Contract(contractAddress, maverickAbi, rpcProviderProxy.provider)

  const price = await poolInfoContract.getPoolPrice(contractAddress)

  const [baseTokenAddress, quoteTokenAddress] = await Promise.all([poolContract.tokenA(), poolContract.tokenB()])
  const [base, quote] = await getERC20TokenInfo([baseTokenAddress, quoteTokenAddress], rpcProviderProxy.provider)

  const decimals_0 = Number(base.decimal)
  const decimals_1 = Number(quote.decimal)

  const scale0 =  Number(await poolContract.tokenAScale())
  const scale1 =  Number(await poolContract.tokenBScale())

  const statePrice = 1 / (Number(price)*1/Math.sqrt(10**decimals_0*scale0*10**decimals_1*scale1)  )

  const prices: PoolPrice[] = [
    {
      base: base.symbol,
      quote: quote.symbol,
      state_price: statePrice,
      pool_address: contractAddress,
      block_number: blockNumber,
    },
  ]
  return prices
}

export default (async ({ context }) => {
  const { logger, vars } = context
  const { network, poolInfoContract, rpcNodeId } = vars

  const rpcProviderProxy = await getRpcProviderProxy(logger, network, rpcNodeId)

  const calculateStatePrice = async (blockNumber: number, contractAddress: string) => {
    return await getPoolTokenRate(poolInfoContract, contractAddress, blockNumber, rpcProviderProxy)
  }
  await evmLogsProcessor(calculateStatePrice, context)
}) as CustomScript
