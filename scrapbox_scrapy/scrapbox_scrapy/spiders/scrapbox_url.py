import scrapy
import scrapy_splash
from scrapbox_scrapy.items import ScrapboxScrapyItem

LUA_SCRIPT = """
function main(splash)
    splash.private_mode_enabled = false
    splash:go(splash.args.url)
    splash:wait(1)
    splash.private_mode_enabled = true
    html = splash:html()
    return html
end
"""


class ScrapboxUrlSpider(scrapy.Spider):
    name = 'scrapbox_url'
    allowed_domains = ['scrapbox.io']
    start_url = ''

    def __init__(self, *args, **kwargs):
        super(ScrapboxUrlSpider, self).__init__(*args, **kwargs)


    def start_requests(self):
        if self.start_url != '':
            yield scrapy_splash.SplashRequest(
                self.start_url,
                self.parse,
                endpoint='execute',
                args={'lua_source': LUA_SCRIPT},
            )

    def parse(self, response):
        for uls in response.css('ul.page-list'):
            for hrefs in uls.css('a'):
                yield ScrapboxScrapyItem(
                    title = hrefs.css('a::text').extract_first(),
                    url = response.urljoin(hrefs.css('a::attr(href)')
                    .extract_first())
                )

