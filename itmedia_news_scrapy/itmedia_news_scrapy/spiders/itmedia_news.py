import scrapy
from itmedia_news_scrapy.items import ItmediaNewsScrapyItem


class ItmediaNewsSpider(scrapy.Spider):
    name = 'itmedia_news'
    allowed_domains = ['www.itmedia.co.jp']
    start_urls = ['https://www.itmedia.co.jp/news/subtop/archive/']

    def parse(self, response):
        for lists in response.css('div.colBoxBacknumber'):
            for links in lists.css('a::attr(href)'):
                detail_link = response.urljoin(links.extract())
                yield scrapy.Request(detail_link, callback=self.detail_parse)

    def detail_parse(self, response):
        content = ''
        for inners in response.css('div.inner p').xpath('node()'):
            content += inners.extract() + '\n'

        yield ItmediaNewsScrapyItem(
            title=response.css('span.title__maintext::text').extract_first(),
            content=content
        )
