import scrapy


class TechbookfestScrapyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    money1 = scrapy.Field()
    money2 = scrapy.Field()
    money3 = scrapy.Field()
    money4 = scrapy.Field()
    openning = scrapy.Field()