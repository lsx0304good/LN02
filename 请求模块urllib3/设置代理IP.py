import urllib3

url = 'http://httpbin.org/ip'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}
# 设置代理管理对象
proxy = urllib3.ProxyManager('http://120.27.110.143:80', headers=headers)
r = proxy.request('GET', url, timeout=2.0)
print(r.data.decode())