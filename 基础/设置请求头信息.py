import urllib.request
import urllib.parse

url = 'https://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

r = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(r)
print(response.read().decode('utf-8'))