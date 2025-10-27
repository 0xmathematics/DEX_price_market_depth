CREATE DATABASE dapps_contract
  LC_COLLATE = 'en_US.UTF-8'
  LC_CTYPE = 'en_US.UTF-8'
  TEMPLATE = template0;


CREATE TABLE smart_contracts_abi (
    id SERIAL PRIMARY KEY,
    blockchain varchar(20) NOT NULL,              -- e.g. Ethereum, BNB, Polygon
	project_name varchar(20) NOT NULL,           -- Human-readable name
    contract_name varchar(20) NOT NULL,           -- Human-readable name
    contract_address varchar(42) UNIQUE NOT NULL, -- Contract address (often checksum format)
    abi JSONB NOT NULL,                    -- The ABI stored as JSONB for querying
    created_at TIMESTAMPTZ DEFAULT now()
);


'''
# SQL command line
 \list 	view all database
 \dt 	view all tables within current databases

 DROP TABLE IF EXISTS my_table CASCADE;

'''