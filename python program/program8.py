# Q8. Create a Pandas DataFrame with a MultiIndex (hierarchical index).
# Perform basic indexing and slicing operations.

import pandas as pd

index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 2)],
    names=['Category', 'Number']
)

df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)

print("Complete DataFrame:\n", df)
print("Category A:\n", df.loc['A'])
print("Specific row:\n", df.loc[('B', 1)])
print("Slicing:\n", df.loc['A':'B'])