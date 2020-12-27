import scrapy


class ScrapboxScrapyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
