# Q2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers.
# Compute the row-wise and column-wise sum.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(4, 3)),
                  columns=['A', 'B', 'C'])
print("Row-wise sum:\n", df.sum(axis=1))
print("Column-wise sum:\n", df.sum(axis=0))