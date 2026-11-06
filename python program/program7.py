# Q7. Create two Pandas DataFrames with a common column.
# Merge the DataFrames using the common column.

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ali', 'John', 'Sara']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Marks': [85, 90, 78]
})

result = pd.merge(df1, df2, on='ID')
print(result)