import urllib.parse

# 方法一：urlencode()，只接受字典类型
base_url = 'http://httpbin.org/get?'
params = {'name': 'Simon', 'country': '中国', 'age': 24}
url = base_url + urllib.parse.urlencode(params)
print('方法一编码后为', url)

# 方法二：quote()，可接受字符串
base_url2 = 'http://httpbin.org/get?country='
url2 = base_url2 + urllib.parse.quote('中国')
print('方法一编码后为', url2)

# unquote()解码，适用于以上两种编码
test1 = urllib.parse.urlencode({'country': '中国'})
test2 = urllib.parse.quote('country=中国')
print('源码1：', test1)
print('解码1：', urllib.parse.unquote(test1))
print('源码2：', test2)
print('解码2：', urllib.parse.unquote(test2))

