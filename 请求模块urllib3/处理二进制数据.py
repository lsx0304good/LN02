import urllib3

urllib3.disable_warnings()
url = 'http://sck.rjkflm.com:666/spider/file/python.png'
http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.data)
f = open('python.png', 'wb+')
f.write(r.data)
f.close()
