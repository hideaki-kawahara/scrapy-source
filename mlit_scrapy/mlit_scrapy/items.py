import scrapy


class MlitScrapyItem(scrapy.Item):
    licence = scrapy.Field()
    company = scrapy.Field()
    address = scrapy.Field()
