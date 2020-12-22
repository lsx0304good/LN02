import urllib.request

url = 'https://www.httpbin.org/get'
proxy_handler = urllib.request.ProxyHandler({
    'https': '58.220.95.114:10053'  # 随机代理IP
})

opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url, timeout=2)
print(response.read().decode('utf-8'))