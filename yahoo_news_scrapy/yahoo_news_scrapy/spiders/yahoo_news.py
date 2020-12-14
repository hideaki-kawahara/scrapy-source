import scrapy
from yahoo_news_scrapy.items import YahooNewsScrapyItem

class YahooNewsSpider(scrapy.Spider):
    name = 'yahoo_news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/topics/it']

    def parse(self, response):
        for items in response.css('li.newsFeed_item'):
            yield YahooNewsScrapyItem(
                url=items.css('a.newsFeed_item_link::attr(href)').extract_first(),
                title=items.css('div.newsFeed_item_title::text').extract_first()
            )
