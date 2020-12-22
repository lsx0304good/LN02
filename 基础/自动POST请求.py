import urllib.request
import urllib.parse

url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
data = bytes(urllib.parse.urlencode({'username': 'lsx0304good', 'password': 'lisixiang945'}), encoding='utf-8')

r = urllib.request.Request(url=url, data=data, method='POST')
response = urllib.request.urlopen(r)
print(response.read().decode('utf-8'))