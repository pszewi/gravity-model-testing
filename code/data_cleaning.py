import pandas as pd
import numpy as np

# if you want to run it as a jupyter notebook file you have to add "..\" in front of data
df_gravity = pd.read_csv("..\data\Gravity_V202211.csv", chunksize=2000)

gravity_new = pd.DataFrame()

# cols to select 
cols = ['year', 'iso3_d','iso3_o', 'distw_arithmetic', \
        'gdp_ppp_pwt_d','gdp_ppp_pwt_o','tradeflow_imf_d', 'tradeflow_imf_o']

# loading the dataset
for chunk in df_gravity:
    subset = chunk[chunk['year'] >= 2000][cols].dropna()
    gravity_new = pd.concat([gravity_new,subset])

# list of oecd countries
oecd_iso = ['AUT', 'BEL', 'CAN', 'CHE', 'CHL', 'COL', 'CRI', 'CZE', 'DEU',
       'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HUN', 'IRL',
       'ISL', 'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LUX', 'LVA', 'MEX',
       'NLD', 'NOR', 'NZL', 'POL', 'PRT', 'SVK', 'SVN', 'SWE', 'TUR',
       'USA', 'AUS']

# subsetting for oecd countries
gravity_new = gravity_new[(gravity_new['iso3_d'].isin(oecd_iso)) & (gravity_new['iso3_o'].isin(oecd_iso))]

