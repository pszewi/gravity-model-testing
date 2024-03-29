import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

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

# making fixed effects dummies


# log transformations of variables for regression
gravity_new['log_dist'] = np.log(gravity_new['distw_arithmetic'])
gravity_new['log_trade_d'] = np.log(gravity_new['tradeflow_imf_d'])
gravity_new['log_trade_o'] = np.log(gravity_new['tradeflow_imf_o'])
gravity_new['log_gdp_d'] = np.log(gravity_new['gdp_ppp_pwt_d'])
gravity_new['log_gdp_o'] = np.log(gravity_new['gdp_ppp_pwt_o'])

# logged tradeflow reported by exporter to distance
sns.lmplot(x='distw_arithmetic', y='log_trade_d',data=gravity_new, col='year', col_wrap=3)
plt.show()


# trying to regress the standard gravity model 
reg1 = sm.ols(formula='log_trade_o ~ log_gdp_o + log_gdp_d + log_dist', data=gravity_new[gravity_new['year']==2009]).fit()
print(reg1.summary())