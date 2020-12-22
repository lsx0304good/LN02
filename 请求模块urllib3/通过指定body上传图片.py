import urllib3

with open('python.jpg', 'rb') as f:
    data = f.read()
http = urllib3.PoolManager()
r = http.request('POST', 'http://httpbin.org/post', body=data, headers={'Content-Type': 'image/jpeg'})
print(r.data.decode())