import urllib3

urllib3.disable_warnings()
url = 'https://httpbin.org/get'
http = urllib3.PoolManager()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}
r = http.request('GET', url, headers=headers)
print(r.data.decode('utf-8'))