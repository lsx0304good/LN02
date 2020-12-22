import pandas as pd

data = pd.read_csv('test.csv')
print('读取内容为：\n', data)

data.to_csv('new_test.csv', columns=['B', 'C'], index=False)
new_data = pd.read_csv('new_test.csv')
print('读取的新CSV内容为：\n', new_data)
