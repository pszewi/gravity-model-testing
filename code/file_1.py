import pandas as pd

# idk what you're working in but I would recommend opening this with "display(next(df_gravity))" (only works with set chunksize)
# because this file is overwhelmingly big  
# also don't open those files with spreadsheets because this will crash your laptop
df_gravity = pd.read_csv("../data\Gravity_V202211.csv", index_col=['year'], chunksize=200)

# display(next(df_gravity))
