# Q12. Create a Pandas Series with 5 random text strings.
# Convert all the strings to uppercase.

import pandas as pd

s = pd.Series(['apple', 'mango', 'orange', 'grapes', 'banana'])
print(s.str.upper())