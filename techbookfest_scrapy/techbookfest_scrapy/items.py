# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TechbookfestScrapyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    money1 = scrapy.Field()
    money2 = scrapy.Field()
    money3 = scrapy.Field()
    money4 = scrapy.Field()
    openning = scrapy.Field()