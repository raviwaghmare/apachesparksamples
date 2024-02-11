import pandas as pd
import numpy as np
#s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

dtypes = ['int64', 'float64', 'complex128', 'object', 'bool']
data = dict([(t, np.ones(shape=5000, dtype=int).astype(t))
             for t in dtypes])
df = pd.DataFrame(data)
print(df)

print(df.memory_usage())