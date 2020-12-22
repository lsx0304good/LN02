from requests_html import HTMLSession, UserAgent

session = HTMLSession()
ua = UserAgent().random
r = session.get('http://news.youth.cn/jsxw/index.htm', headers={'User-Agent': ua})
r.encoding = 'gb2312'

if r.status_code == 200:
    li_all = r.html.xpath('.//ul[@class="tj3_1"]/li')
    for li in li_all:
        news_title = li.find('a')[0].text
        news_href = 'http://news.youth.cn/jsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('.')
        news_time = li.find('font')[0].text
        # print(li.find('a[href]')[0].attrs.get('href').lstrip('.'))
        print('新闻标题：', news_title)
        print('新闻网址：', news_href)
        print('发布时间：', news_time)