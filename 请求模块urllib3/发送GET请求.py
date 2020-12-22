import urllib3

url = "http://httpbin.org/get"
http = urllib3.PoolManager()  # 创建连接池管理对象
r = http.request('GET', url)
print(r.status)

urllib3.disable_warnings()  # 关闭ssl警告
jingdong_url = 'https://www.jd.com/'
python_url = 'https://www.python.org/'
baidu_url = 'https://www.baidu.com/'
http = urllib3.PoolManager()
r1 = http.request('GET', jingdong_url)
r2 = http.request('GET', python_url)
r3 = http.request('GET', baidu_url)
print('京东请求状态码：', r1.status)
print('Python请求状态码：', r2.status)
print('百度请求状态码：', r3.status)