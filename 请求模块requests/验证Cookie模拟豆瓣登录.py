import requests
from lxml import etree

cookies = 'bid=41DaOWshtbQ; douban-fav-remind=1; __utmz=30149280.1595035601.1.1.utmcsr=baidu|utmccn=(' \
          'organic)|utmcmd=organic; ll="108090"; ' \
          '_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1607664407%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl' \
          '%3DnGH9ChPdV0Tx_Zx5gN_Y2ydmw_soHaGD6hQVPtgPNnmnD5QVeU_XsdO' \
          '-zxzgbAaMGiHL6ZTTvzSiytiF2WFLGO0XEQPnCqDrUGzgnOwevTG%26wd%3D%26eqid%3De2396951000716ca000000025f124fcc%22' \
          '%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1152559733.1595035601.1595035601.1607664416.2; ' \
          '__utmc=30149280; __utmt=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22816; ap_v=0,' \
          '6.0; _pk_id.100001.8cb4=227fb702da423a27.1595035601.2.1607664476.1595035605.; ' \
          '__utmb=30149280.4.10.1607664416; dbcl2="228166240:EUAknVbfC0E" '

headers = {'Host': 'www.douban.com',
           'Referer': 'https://www.hao123.com/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.66 Safari/537.36',
           }

cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    cookies_jar.set(key, value)

response = requests.get('https://www.douban.com/', headers=headers, cookies=cookies_jar)
if response.status_code == 200:
    html = etree.HTML(response.text)
    name = html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0])