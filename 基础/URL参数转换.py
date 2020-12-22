import urllib.parse
# 转换为字典类型
url = 'http://httpbin.org/get?name=Simon&country=%E4%B8%AD%E5%9B%BD&age=24'
q = urllib.parse.urlsplit(url).query  # 获取参数
q_dict = urllib.parse.parse_qs(q)  # 将参数转换为字典类型的数据
print('数据类型为：', type(q_dict))
print('转换后：', q_dict)

# 转换为列表类型
str_params = 'name=Simon&country=%E4%B8%AD%E5%9B%BD&age=24'
list_params = urllib.parse.parse_qsl(str_params)  # 转化为元组所组成的列表
print('数据类型为：', type(list_params))
print('转换后：', list_params)