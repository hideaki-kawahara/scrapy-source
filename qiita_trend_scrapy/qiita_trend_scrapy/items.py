import scrapy


class QiitaTrendScrapyItem(scrapy.Item):
    keyword = scrapy.Field()
    count = scrapy.Field()
