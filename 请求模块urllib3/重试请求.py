import urllib3

urllib3.disable_warnings()
url = 'https://www.httpbin.org/get'
http = urllib3.PoolManager()
r = http.request('GET', url)
r1 = http.request('GET', url, retries=5)
r2 = http.request('GET', url, retries=False)
print('默认重试请求次数：', r.retries.total)
print('设置重试请求次数：', r1.retries.total)
print('关闭重试请求次数：', r2.retries.total)
