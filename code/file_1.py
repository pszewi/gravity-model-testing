import pandas as pd

df_gravity = pd.read_csv("../data\Gravity_V202211.csv", index_col=['year'], chunksize=200)

nums = [1,2,3,4,5,6,7]
