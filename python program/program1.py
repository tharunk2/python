# Q1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers.
# Add a new column that is the product of the first two columns.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)),
                  columns=['A', 'B', 'C'])
df['Product'] = df['A'] * df['B']
print(df)