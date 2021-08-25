import scrapy


class ItmediaNewsScrapyItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

