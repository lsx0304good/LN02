# 使用render.html接口获取百度首页图片链接
import requests
from bs4 import BeautifulSoup

splash_url = 'http://localhost:8050/render.html'
args = {'url': 'https://www.baidu.com/'}
response = requests.get(splash_url, args)
response.encoding='utf-8'
bs = BeautifulSoup(response.text, "html.parser")
img_url = 'https:' + bs.select('div[class="s-p-top"]')[0].select('img')[0].attrs['src']
print(img_url)

# 使用render.png接口获取
splash_url2 = 'http://localhost:8050/render.png'
args2 = {'url': 'https://www.baidu.com/', 'width':1280, 'height':800}
response2 = requests.get(splash_url2, args2)
with open('baidu.png', 'wb') as f:
    f.write(response2.content)