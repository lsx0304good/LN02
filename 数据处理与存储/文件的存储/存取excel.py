import pandas as pd

# save
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
df.to_excel('test.xlsx')

# load
data_load = pd.read_excel('test.xlsx')
print('内容为：\n', data_load)
