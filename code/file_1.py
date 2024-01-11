import pandas as pd
import numpy as np

df_gravity = pd.read_csv("data\Gravity_V202211.csv", chunksize=200, nrows=10_000)

gravity_new = pd.DataFrame()

cols = ['year', 'country_id_d','country_id_o', 'distw_arithmetic',  
        'gdp_ppp_pwt_d','gdp_ppp_pwt_o','tradeflow_imf_d', 'tradeflow_imf_o']

for chunk in df_gravity:
    subset = chunk[chunk['year'] >= 2000][cols].dropna()
    gravity_new = pd.concat([gravity_new,subset])

print(gravity_new.shape)



