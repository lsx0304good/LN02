import urllib3
import json

with open('test.txt') as f:
    data = f.read()
http = urllib3.PoolManager()
r = http.request('POST', 'http://httpbin.org/post', fields={'filefield': ('example.txt', data),})
files = json.loads(r.data.decode('utf-8'))['files']
print(files)