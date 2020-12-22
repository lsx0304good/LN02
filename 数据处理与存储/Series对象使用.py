import pandas as pd

data = ['A', 'B', 'C']
index = ['a', 'b', 'c']
series = pd.Series(data, index=index)
print(series[['a', 'c']])
print(series.index)
print(series.values)