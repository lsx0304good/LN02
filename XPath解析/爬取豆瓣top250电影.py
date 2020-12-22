from lxml import etree
import time
import random
import requests

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}


# 处理大量空白符
def processing(strs):
    s = ''
    for n in strs:
        n = ''.join(n.split())
        s += n
    return s


# 获取电影信息
def get_movie_info(url):
    response = requests.get(url, headers=header)
    html = etree.HTML(response.text)
    print(html)
    div_all = html.xpath('//div[@class="info"]')
    print(div_all)
    for div in div_all:
        names = div.xpath('./div[@class="hd"]/a//span/text()')
        name = processing(names)
        infos = div.xpath('./div[@class="bd"]/p/text()')
        info = processing(infos)
        score = div.xpath('./div[@class="bd"]/div/span[2]/text()')[0]
        evaluation = div.xpath('./div[@class="bd"]/div/span[4]/text()')[0]
        try:
            summary = div.xpath('./div[@class="bd"]/p[2]/span/text()')[0]
        except IndexError:
            summary = '暂无评价'
        print('电影名称：', name)
        print('导演与演员：', info)
        print('评分：', score)
        print('评价人数：', evaluation)
        print('电影总结：', summary)
        print('\n')


if __name__ == "__main__":
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={page}&filter='.format(page=i)
        get_movie_info(url)