# Q3. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers.
# Introduce some NaN values. Fill the NaN values with the mean of the respective columns.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)),
                  columns=['A', 'B', 'C'])
df.loc[1, 'A'] = np.nan
df.loc[2, 'B'] = np.nan
df.loc[3, 'C'] = np.nan

print("Before filling:\n", df)
df = df.fillna(df.mean())
print("After filling:\n", df)