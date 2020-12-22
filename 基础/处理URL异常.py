import urllib.request
import urllib.error

try:
    # 向不存在的地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
except urllib.error.URLError as error:
    print(error.reason)