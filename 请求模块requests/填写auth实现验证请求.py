import requests
from requests.auth import HTTPBasicAuth

url = 'http://sck.rjkflm.com:666/spider/auth/'
ah = HTTPBasicAuth('admin', 'admin')
response = requests.get(url=url, auth=ah)
if response.status_code == 200:
    print(response.text)