from lxml import etree
import time
import random
import requests


header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}

url = 'https://www.bilibili.com/v/popular/rank/all'
def processing(strs):
    s = ''
    for n in strs:
        n = ''.join(n.split())
        s += n
    return s

response = requests.get(url, headers=header)
html = etree.HTML(response.text)
li_all = html.xpath('//li[@class="rank-item"]')
for li in li_all:
    name = li.xpath('./div[@class="content"]/div[@class="info"]/a/text()')[0]
    author = li.xpath('./div[@class="content"]/div[@class="info"]/div[@class="detail"]/a/span/text()')[0]
    score = li.xpath('./div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()')[0]
    plays = li.xpath('./div[@class="content"]/div[@class="info"]/div[@class="detail"]/span[1]/text()')[0]
    comments = li.xpath('./div[@class="content"]/div[@class="info"]/div[@class="detail"]/span[2]/text()')[0]
    print('标题：', name)
    print('作者：', processing(author))
    print('评分', score, '分')
    print('播放量：', processing(plays), '次')
    print('弹幕：', processing(comments), '条')
    print('\n')
