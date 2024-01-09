import pandas as pd


df_gravity = pd.read_csv("data\Gravity_V202211.csv", index_col=['year'], chunksize=200)

# working with "print(next(df_gravity))" allows you to load the file in 'chunks' (note the 'chunksize' in pd.read_csv)  
# i.e. every time you copy and paste this command it will print another chunk 
print(next(df_gravity))
# print(next(df_gravity)) can see for yourself :)
# print(next(df_gravity))