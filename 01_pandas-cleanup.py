# clean up items by specific check through iteration
import numpy as np
import pandas as pd

# read huge dataset file
# na_values includes NA but not all NA Values
# user can always add other custom NA like n.a., ?, etc
d_set = pd.read_csv('auto-data.csv')

# cleaning up dataframe using iteration
# perform iteration via columns and index
# chck on each items and replace the values
for col in d_set.columns:
    for i in d_set.index:
        value = d_set.at[i, col]
        if (value == "?" or value == "n.a."):
            # print Row, Column and Value for checking
            print(f"Row= {i}, Col= {col}, Value= {value}")
            d_set.at[i, col] = np.nan # Assigned as NaN

#Export back to CSV file name "aut_op_iterupdate.csv"
d_set.to_csv('auto_op_iterupdate.csv', index=False)

