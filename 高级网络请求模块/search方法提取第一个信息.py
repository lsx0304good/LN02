from requests_html import HTMLSession, UserAgent

session = HTMLSession()
ua = UserAgent().random
r = session.get('http://news.youth.cn/jsxw/index.htm', headers={'User-Agent': ua})
r.encoding = 'gb2312'

if r.status_code == 200:
    for li in r.html.find('li', containing='疫情'):
        a = li.search('<a href="{}>{}</a>')
        # print(a)
        news_title = a[1]
        news_href = 'http://news.youth.cn/jsxw' + a[0].lstrip('.')
        news_time = li.search('<font>{}</font>')[0]
        # print(li.find('a[href]')[0].attrs.get('href').lstrip('.'))
        print('新闻标题：', news_title)
        print('新闻网址：', news_href)
        print('发布时间：', news_time)