# Q4. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers.
# Introduce some NaN values. Drop the rows with any NaN values.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(6, 4)),
                  columns=['A', 'B', 'C', 'D'])
df.loc[1, 'A'] = np.nan
df.loc[3, 'C'] = np.nan

print("Before dropping:\n", df)
df = df.dropna()
print("After dropping:\n", df)