# Q6. Create a DataFrame with Product, Category, and Sales columns.
# Fill the DataFrame with random data. Group by Category and compute total sales.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': np.random.choice(['Pen', 'Book', 'Bag'], size=8),
    'Category': np.random.choice(['Stationery', 'Accessories'], size=8),
    'Sales': np.random.randint(100, 1000, size=8)
})

print(df)
print(df.groupby('Category')['Sales'].sum())