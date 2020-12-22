from lxml import etree
import requests
from requests.auth import HTTPBasicAuth

url = 'http://sck.rjkflm.com:666/spider/auth'
ah = HTTPBasicAuth('admin', 'admin')
response = requests.get(url=url, auth=ah)
if response.status_code == 200:
    html = etree.HTML(response.text)
    html_txt = etree.tostring(html, encoding='utf-8')
    print(html_txt.decode('utf-8'))