import scrapy


class HatenaBookmarksScrapyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    bookmark_count = scrapy.Field()
    bookmark_url = scrapy.Field()
