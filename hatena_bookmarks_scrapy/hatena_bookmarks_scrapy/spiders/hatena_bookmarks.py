import scrapy
from hatena_bookmarks_scrapy.items import HatenaBookmarksScrapyItem


class HatenaBookmarksSpider(scrapy.Spider):
    name = 'hatena_bookmarks'
    allowed_domains = ['b.hatena.ne.jp']
    start_urls = ['https://b.hatena.ne.jp/hotentry/it']


    def parse(self, response):
        for items in response.css('div.entrylist-contents'):
            yield HatenaBookmarksScrapyItem(
                title=items.css('h3.entrylist-contents-title a::attr(title)').extract_first(),
                url=items.css('h3.entrylist-contents-title a::attr(href)').extract_first(),
                bookmark_count=int(items.css('span.entrylist-contents-users span::text').extract_first()),
                bookmark_url=response.urljoin(items.css('span.entrylist-contents-users a::attr(href)').extract_first()),
            )
