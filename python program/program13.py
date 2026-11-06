# Q13. Create a Pandas Series with 5 random text strings.
# Extract the first three characters of each string.

import pandas as pd

s = pd.Series(['apple', 'mango', 'orange', 'grapes', 'banana'])
print(s.str[:3])