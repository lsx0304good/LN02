import requests

response = requests.get('https://www.baidu.com')
print('响应状态码：', response.status_code)
print('请求网络地址：', response.url)
print('头部信息：', response.headers)
print('Cookie信息：', response.cookies)

# 获取网络源码
response.encoding = 'utf-8'
print(response.text)
