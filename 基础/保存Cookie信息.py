import urllib.request
import urllib.parse
import http.cookiejar
import json

url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
data = bytes(urllib.parse.urlencode({'username': 'lsx0304good', 'password': 'lisixiang945'}), encoding='utf-8')
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(cookie_file)
# 生成Cookie处理器
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener对象
opener = urllib.request.build_opener(cookie_processor)
response = opener.open(url, data=data)
response = json.loads(response.read().decode('utf-8'))['msg']

if response == "登录成功！":
    # 保存Cookie文件
    cookie.save(ignore_discard=True, ignore_expires=True)