import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}
proxy = {'http': 'http://117.88.176.38:3000',
         'https': 'https://117.88.176.38:3000',
         }
try:
    response = requests.get('http://202020.ip138.com',
                            headers=headers,
                            proxies=proxy,
                            verify=False,  # 不验证服务器SSL证书
                            timeout=3,
                            )
except Exception as e:
    print('错误信息为：', e)