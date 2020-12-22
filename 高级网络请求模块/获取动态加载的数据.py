from requests_html import HTMLSession, UserAgent

session = HTMLSession()
ua = UserAgent().random

r = session.get('https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E6%82%AC%E7%96%91', headers={'User-Agent': ua})
r.encoding = 'gb2312'
if r.status_code == 200:
    r.html.render()

class_wp = r.html.xpath('.//div[@class="list-wp"]/a')
for a in class_wp:
    title = a.find('p span')[0].text
    rate = a.find('p span')[1].text
    details_url = a.attrs.get('href')
    img_url = a.find('img')[0].attrs.get('src')
    print('\n')
    print('电影名称：', title)
    print('电影评分：', rate)
    print('详情页地址：', details_url)
    print('图片地址：', img_url)
