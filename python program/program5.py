# Q5. Create a DataFrame with two columns: Category and Value.
# Fill Category with random categories A, B, C and Value with random integers.
# Group by Category and compute the sum and mean of Value.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(10, 100, size=10)
})

print(df.groupby('Category')['Value'].agg(['sum', 'mean']))