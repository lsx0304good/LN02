import re
from requests_html import HTMLSession, UserAgent

session = HTMLSession()
ua = UserAgent().random
r = session.get('http://news.youth.cn/jsxw/index.htm', headers={'User-Agent': ua})
r.encoding = 'gb2312'
class_tj3_1 = r.html.xpath('.//ul[@class="tj3_1"]')
li_all = class_tj3_1[0].search_all('<li>{}</li>')
for li in li_all:
    if '疫情' in li[0]:
        # print(li[0])
        a = re.findall('<font>(.*?)</font><a href="(.*?)">(.*?)</a>', li[0])
        # print(a)
        news_title = a[0][2]
        news_href = 'http://news.youth.cn/jsxw' + a[0][1].lstrip('.')
        news_time = a[0][0]
        print('新闻标题：', news_title)
        print('新闻网址：', news_href)
        print('发布时间：', news_time)