import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# if you want to run it as a jupyter notebook file you have to add "..\" in front of data
df_gravity = pd.read_csv("data\Gravity_V202211.csv", chunksize=2000)

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

# log transformations of variables for regression
gravity_new['log_dist'] = np.log(gravity_new['distw_arithmetic'])
gravity_new['log_trade_d'] = np.log(gravity_new['tradeflow_imf_d'])
gravity_new['log_trade_o'] = np.log(gravity_new['tradeflow_imf_o'])
gravity_new['log_gdp_d'] = np.log(gravity_new['gdp_ppp_pwt_d'])
gravity_new['log_gdp_o'] = np.log(gravity_new['gdp_ppp_pwt_o'])

# making fixed effects dummies
dummies = pd.get_dummies(gravity_new[['iso3_o', 'iso3_d']], prefix=['o','d'])
gravity_new = gravity_new.join(dummies)

# base for the regression equation
reg_expression = 'log_trade_o ~ log_gdp_o + log_gdp_d + log_dist'
dumm_names = dummies.columns

# a for loop to add all of the dummies to the regression equation
for i in range(len(dumm_names)):
    if (dumm_names[i] == 'o_USA') | (dumm_names[i] == 'd_USA'):
        continue
    elif dumm_names[i]:
        reg_expression = reg_expression + ' + ' + dumm_names[i]
    else:
        None

# trying to regress the standard gravity model 
reg1 = sm.ols(formula=reg_expression, data=gravity_new).fit()
print(reg1.summary())
