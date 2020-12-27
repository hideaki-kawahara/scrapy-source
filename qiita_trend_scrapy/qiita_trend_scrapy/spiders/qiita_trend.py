import scrapy
from qiita_trend_scrapy.items import QiitaTrendScrapyItem
from qiita_trend_scrapy.database import session ,Base
from qiita_trend_scrapy.tag import Tag


class QiitaTrendSpider(scrapy.Spider):
    name = 'qiita_trend'
    allowed_domains = ['qiita.com']
    start_urls = ['http://qiita.com/']

    def parse(self, response):
        keywords = {}
        for items in response.css('a.css-4czcte'):
            key = items.css('a.css-4czcte::text').extract_first()
            if (key in keywords.keys()):
                keywords[key] = keywords[key] + 1
            else:
                keywords[key] = 1

        for keyword, count in keywords.items():
            yield QiitaTrendScrapyItem(keyword = keyword, count = count)
