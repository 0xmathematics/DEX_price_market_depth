create table dex_trade (
    amount0 DECIMAL(78),
    amount1 DECIMAL(78),
    contract_address VARCHAR(42),
    evt_block_number BIGINT,
    evt_block_time TIMESTAMPTZ,
    evt_index INTEGER,
    evt_tx_hash VARCHAR(66),
    liquidity DECIMAL(78),
    recipient VARCHAR(42),
    sender VARCHAR(42),
    sqrtPriceX96 DECIMAL(78),
    tick INTEGER
)

COPY public.DEX_TRADE (
	AMOUNT0,
	AMOUNT1,
	CONTRACT_ADDRESS,
	EVT_BLOCK_NUMBER,
	EVT_BLOCK_TIME,
	EVT_INDEX,
	EVT_TX_HASH,
	LIQUIDITY,
	RECIPIENT,
	SENDER,
	SQRTPRICEX96,
	TICK
)
FROM
	'/Users/yeminlan/Desktop/trino_db_pwd/WBTC_ETH_500/uniswap_WBTC_ETH_500_ETH_05-06-2021_08-20-2022_SWAP.csv' 
	DELIMITER ',' 
	CSV HEADER;

select *  from dex_trade limit 10
select count(*) AS number_entry  from dex_trade 

SHOW DATA_DIRECTORY;
