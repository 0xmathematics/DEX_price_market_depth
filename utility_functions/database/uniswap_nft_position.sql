
with nft_position as (
select t1.blockchain, project_name, t2.symbol as base, t3.symbol as quote, fee, token_id, t1.address, token0,token1,tick_lower,tick_upper,liquidity,
fee_growth_inside0_last_x128,fee_growth_inside1_last_x128,tokens_owed0,tokens_owed1,owner_address


from uniswap_lp_position  t1
left join erc20_token t2
on t1.token0 = t2.address
left join erc20_token t3
on t1.token1 = t3.address
where liquidity>0

)

select *
from nft_position
