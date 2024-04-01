import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from data_cleaning import gravity_new

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
reg_expression = 'log_trade_o ~ log_gdp_o + log_gdp_d + log_dist + year'
dumm_names = dummies.columns

# a for loop to add all of the dummies to the regression equation
# US is most probably not suitable for the base dummy since it's the US
for i in range(len(dumm_names)):
    if (dumm_names[i] == 'o_USA') | (dumm_names[i] == 'd_USA'):
        continue
    elif dumm_names[i]:
        reg_expression = reg_expression + ' + ' + dumm_names[i]
    else:
        None

# trying to regress the standard gravity model 
reg1 = sm.ols(formula=reg_expression, data=gravity_new).fit(cov_type='HAC', cov_kwds={'maxlags':1})
print(reg1.summary())


