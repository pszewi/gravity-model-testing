import pandas as pd
import numpy as np 
import statsmodels.api as sm

df_gravity = pd.read_csv("data\Gravity_V202211.csv", index_col=['year'], chunksize=200)

# working with "print(next(df_gravity))" allows you to load the file in 'chunks' (note the 'chunksize' in pd.read_csv)  
# i.e. every time you copy and paste this command it will print another chunk 


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df_grav = pd.read_csv('data\Gravity_V202211.csv', index_col=0)
df = pd.DataFrame(df_grav)
df_1 = df.loc[:, ['iso3_o', 'iso3_d', 'country_exists_o', 'country_exists_d', 'distw_arithmetic', 'gdp_o', 'gdp_d', 'tradeflow_baci']]  # selection of relevant columns
df_2 = df_1[(df_1['country_exists_o'] != 0) & (df_1['country_exists_d'] != 0)]  # keep only observations where both countries existed
df_3 = df_2[((df_2['iso3_o'] == 'USA') & (df_2['iso3_d'] == 'CHN'))]    # for a test, keep only USA and CHN (CHN&USa leads to the same) - check how to do regressions with panel data
df_4 = df_3.dropna(axis=0, how='any')
print(df_4)
df_4[['gdp_o', 'gdp_d', 'distw_arithmetic', 'tradeflow_baci']] = np.log(df_4[['gdp_o', 'gdp_d', 'distw_arithmetic', 'tradeflow_baci']]) # convert to log scale
print(df_4)

x = df_4[['gdp_o','gdp_d','distw_arithmetic']]   # independent variables
y = df_4['tradeflow_baci']  # dependent
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
print(model.summary())  # re-check the whole thing (eg R^2 = 1)


