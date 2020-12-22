import urllib3

urllib3.disable_warnings()
url = 'https://httpbin.org/get'
http = urllib3.PoolManager()
r = http.request('GET', url)
response_header = r.info()
for key in response_header.keys():
    print(key, ':', response_header.get(key))
