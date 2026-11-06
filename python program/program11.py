# Q11. Create a Pandas DataFrame with 3 columns and 6 rows filled with random integers.
# Apply a lambda function to create a new column that is the sum of existing columns.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(6, 3)),
                  columns=['A', 'B', 'C'])

df['Sum'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)
print(df)