import requests
from fake_useragent import UserAgent
from multiprocessing import Pool
import re
from bs4 import BeautifulSoup
import time


class Spider():
    def __init__(self):
        self.info_urls = []

    def get_home(self, home_url):
        header = UserAgent().random
        home_response = requests.get(home_url, header)
        if home_response.status_code == 200:
            home_response.encoding = 'gb2312'
            html = home_response.text
            details_urls = re.findall('<a href="(.*?)" class="ulink">', html)
            self.info_urls.extend(details_urls)


    def get_info(self, url):
        header = UserAgent().random
        info_response = requests.get(url, header)
        if info_response.status_code == 200:
            info_response.encoding = 'gb2312'
            html = BeautifulSoup(info_response.text, "html.parser")
        try:
            download_url = re.findall('<a href=".*?">(.*?)</a></td>', info_response.text)[0]
            name = html.select('div[class="title_all"]')[0].text
            info_all = (html.select('div[id="Zoom"]')[0]).p.text.replace('\u3000', '').split('◎')
            date = info_all[8]
            imdb = info_all[9]
            douban = info_all[10]
            length = info_all[14]
            info = {'name': name,
                    'date': date,
                    'imdb': imdb,
                    'douban': douban,
                    'length': length,
                    'download_url': download_url,
                    }
            # print(info)
        except:
            return


if __name__ == '__main__':
    home_url = ['https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i)) for i in range(1, 11)]
    s = Spider()
    start_time = time.time()
    for i in home_url:
        s.get_home(i)
    end_time = time.time()
    print('串行爬取详情页耗时：', end_time - start_time)

    start_time_4 = time.time()
    pool = Pool(processes=4)
    pool.map(s.get_home, home_url)
    end_time_4 = time.time()
    print('4进程爬取详情页耗时：', end_time_4 - start_time_4)


    info_urls = ['https://www.ygdy8.net' + i for i in s.info_urls]
    info_start_time = time.time()
    for i in info_urls:
        s.get_info(i)
    info_end_time = time.time()
    print('串行爬取信息耗时：', info_end_time - info_start_time)

    info_start_time_4 = time.time()
    pool = Pool(processes=4)
    pool.map(s.get_info, info_urls)
    info_end_time_4 = time.time()
    print('4进程爬取信息耗时：', info_end_time_4 - info_start_time_4)
