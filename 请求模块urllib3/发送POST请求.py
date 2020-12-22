import urllib3

urllib3.disable_warnings()  # 关闭ssl警告
url = "http://httpbin.org/post"
params = {'name': 'Simon', 'chinese_name': '李思翔', 'age': 24}
http = urllib3.PoolManager()
r = http.request('POST', url, fields=params)
print('返回结果：', r.data.decode('unicode_escape'))