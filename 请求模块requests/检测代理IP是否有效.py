import requests
import pandas
from lxml import etree

ip_table = pandas.read_excel('ip.xlsx')
ip = ip_table['ip']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}

for i in ip:
    proxies = {'http': 'http://{ip}'.format(ip=i),
               'https': 'https://{ip}'.format(ip=i),
               }
    try:
        response = requests.get('http://202020.ip138.com/',
                                headers=headers,
                                proxies=proxies,
                                timeout=2)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            info = html.xpath('/html/body/p[1]//text()')
            print(info)
    except Exception as e:
        pass