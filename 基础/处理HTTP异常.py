import urllib.request
import urllib.error

try:
    # 向不存在的地址发送请求
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
    print(response.status)
except urllib.error.HTTPError as error:
    print('状态码：', error.code)
    print('异常信息：', error.reason)
    print('请求头信息：\n', error.headers)