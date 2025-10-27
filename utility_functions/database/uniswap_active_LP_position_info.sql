
CREATE MATERIALIZED VIEW active_uniswap_v3_lp_mv AS
with active_LP_state_info as (

SELECT t1.blockchain, t1.address, t1.fee, t1.token_id, 
t1.tick_lower,t1.tick_upper, t1.liquidity,
t2.tick, t2.sqrt_price_x96, 
t3.symbol AS symbol_0, t3.decimals AS decimal_0,  
t4.symbol AS symbol_1, t4.decimals AS decimal_1,
sqrt(1.0001^tick_lower) AS sqrt_p_a,
sqrt(1.0001^tick_upper) AS sqrt_p_b,
t2.sqrt_price_x96/2^96 AS sqrt_p,
t1.fee_growth_inside0_last_x128,
t1.fee_growth_inside1_last_x128,
t5.fee_growth_inside_current_0,
t5.fee_growth_inside_current_1

FROM public.uniswap_lp_position t1 -- *** list of all LP 
left join public.uniswap_pool_state_info t2 -- *** current  state info from pool of interest
on t1.blockchain = t2.blockchain and t1.address = t2.contract_address
left join  public.erc20_token t3  -- erc20 info for token0 
on t1.blockchain = t2.blockchain and t1.token0 = t3.address
left join  public.erc20_token t4  -- erc20 info for token1
on t1.blockchain = t4.blockchain and t1.token1 = t4.address
left join  public.uniswap_lp_state_info t5  -- ***LP state info
on t1.blockchain = t5.blockchain and t1.project_name = t5.project_name and t1.token_id = t5.token_id

where t1.liquidity >0
)
--select * from active_LP_state_info

select blockchain, address,
(sqrt_price_x96/2^96)^2*10^(decimal_0-decimal_1) AS price_01,
1/((sqrt_price_x96/2^96)^2*10^(decimal_0-decimal_1)) AS price_10,
ARRAY[1.0001^tick_lower*10^(decimal_0-decimal_1),
1.0001^tick_upper*10^(decimal_0-decimal_1)] AS range_01,
ARRAY[1/(1.0001^tick_upper*10^(decimal_0-decimal_1)) ,
1/(1.0001^tick_lower*10^(decimal_0-decimal_1))] AS range_10,
fee,symbol_0,symbol_1, 
    -- Compute x based on conditions
    CASE 
        WHEN tick <= tick_lower THEN 
            liquidity * (sqrt_p_b - sqrt_p_a) / (sqrt_p_a * sqrt_p_b)/10^decimal_0
        WHEN tick < tick_upper THEN 
            liquidity * (sqrt_p_b - sqrt_p) / (sqrt_p * sqrt_p_b)/10^decimal_0
        ELSE 
            0
    END AS x,

    -- Compute y based on conditions
    CASE 
        WHEN tick <= tick_lower THEN 
            0
        WHEN tick < tick_upper THEN 
            liquidity * (sqrt_p - sqrt_p_a)/10^decimal_1
        ELSE 
            liquidity * (sqrt_p_b - sqrt_p_a)/10^decimal_1
    END AS y,
liquidity*
(((fee_growth_inside_current_0-fee_growth_inside0_last_x128) % 2^256::numeric + 2^256::numeric )% 2^256::numeric  )
/ CAST(2^128 AS numeric)/10^decimal_0 AS fee_x,
liquidity*
(((fee_growth_inside_current_1-fee_growth_inside1_last_x128) % 2^256::numeric + 2^256::numeric )% 2^256::numeric )
/ CAST(2^128 AS numeric)/10^decimal_1 AS fee_y,


token_id,
    CASE 
        WHEN tick >= tick_lower and tick< tick_upper THEN TRUE
        ELSE False
    END AS in_range


from active_LP_state_info
order by in_range desc

--DROP TABLE IF EXISTS active_uniswap_v3_lp_mv CASCADE;
--REFRESH MATERIALIZED VIEW active_uniswap_v3_lp_mv;


