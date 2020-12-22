import urllib3
import json

urllib3.disable_warnings()
url = 'https://www.httpbin.org/post'
params = {'name': 'Simon', 'country': '中国', 'age': 24}
http = urllib3.PoolManager()
r = http.request('POST', url, fields=params)
j = json.loads(r.data.decode('unicode_escape'))
print('数据类型：', type(j))
print('获取form对应数据：', j.get('form'))
print('获取country对应数据：', j.get('form').get('country'))