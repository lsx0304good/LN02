import scrapy
import json
# 在程序中启动爬虫：
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    data = {'1': '能力有限，努力无限',
            '2': '星光不问赶路人，时光不负有心人', }

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
                ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    #
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    # def start_requests(self):
    #     return [scrapy.FormRequest('http://httpbin.org/post', formdata=self.data, callback=self.parse)]

    # def parse(self, response):
    #     response_dict = json.loads(response.text)
    #     print(response_dict)

    # 使用xpath获取信息
    def parse(self, response):
        for quote in response.xpath(".//*[@class='quote']"):
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            tags = quote.xpath(".//*[@class='tag']/text()").extract()
            item = ScrapydemoItem(text=text, author=author, tags=tags)
            yield item


class ScrapydemoItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    pass



if __name__ == '__main__':
    # 创建对象并传入设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('quotes')
    process.start()
