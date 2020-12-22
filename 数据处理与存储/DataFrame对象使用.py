import pandas as pd
import numpy as np

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        }
df = pd.DataFrame(data)
# print(df)

index = ['a', 'b', 'c', 'd', 'e']
df2 = pd.DataFrame(data, index=index, columns=['B', 'C'])
# print(df2)
df2['C']['c'] = 9
# print(df2)

# delete row
df3 = df
df3.drop([0], inplace=True)
# print(df3)

# delete column
df3 = df
df3.drop(labels='A', axis=1, inplace=True)
# print(df3)

# NaN数据处理
df_nan = pd.DataFrame(data)
df_nan['A'][0] = np.nan
print(df_nan)
print("no. of Nan for each COLUMN: ", df_nan.isnull().sum())
print("no. of non-Nan for each COLUMN: ", df_nan.notnull().sum())

# 删除包含Nan的整行数据
df_nan.dropna(axis=0, inplace=True)
print(df_nan)

# 删除包含Nan的整行数据
df_nan.dropna(axis=1, inplace=True)
print(df_nan)

# 将所有NaN修改为0
df_nan.fillna(0, inplace=True)