# Q9. Create a DataFrame with MultiIndex consisting of Category and SubCategory.
# Fill it with random data and compute the sum of values for each combination.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'SubCategory': ['X', 'Y', 'X', 'X', 'Y', 'Y'],
    'Value': np.random.randint(10, 100, size=6)
})

df = df.set_index(['Category', 'SubCategory'])
print(df.groupby(level=['Category', 'SubCategory']).sum())