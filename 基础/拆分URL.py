import urllib.parse

# 方法一：urlparse
parse_result = urllib.parse.urlparse('https://docs.python.org/3/library/urllib.parse.html')
print(type(parse_result))
print(parse_result)

# 方法二：urlsplit （不单独拆分param）
url = 'https://docs.python.org/3/library/urllib.parse.html'
urlsplit = urllib.parse.urlsplit(url)
print(urlsplit.scheme)
print(urlsplit[0])  # 拆分完成可用索引查询


list1 = [i for i in parse_result]
print('拆分URL: ', list1)
print('重新组合URL: ', urllib.parse.urlunparse(list1))