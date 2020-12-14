import scrapy


class YahooNewsScrapyItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
