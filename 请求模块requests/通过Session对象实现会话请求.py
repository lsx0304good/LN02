import requests

s = requests.Session()
data = {'username': 'lsx0304good', 'password': 'lisixiang945'}
response = s.post('http://site2.rjkflm.com:666/index/index/chklogin.html', data=data)
response2 = s.get('http://site2.rjkflm.com:666')
print('登录信息：', response.text)
print('登录后页面信息：\n', response2.text)