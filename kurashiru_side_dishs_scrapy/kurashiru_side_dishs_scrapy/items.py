import scrapy


class KurashiruSideDishsScrapyItem(scrapy.Item):
    site_url = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()
    cooking_time = scrapy.Field()
    budget = scrapy.Field()
    ingredient = scrapy.Field()
    how_to_make = scrapy.Field()
    tip = scrapy.Field()
