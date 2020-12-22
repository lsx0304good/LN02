import urllib.request
import http.cookiejar

# 登录后的页面请求地址
url = 'http://site2.rjkflm.com:666/index/index/index.html'
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar()
cookie.load(cookie_file, ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(response.read().decode('utf-8'))