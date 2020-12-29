import scrapy
import scrapy_splash
from techbookfest_scrapy.items import TechbookfestScrapyItem


LUA_SCRIPT_LIST = """
function main(splash, args)
  local scroll_to = splash:jsfunc("window.scrollTo")
  splash:go(args.url)
  for _ = 1, 20 do
    scroll_to(0, 10000)
    splash:wait(1)
  end
  html = splash:html()
  return html
end
"""

LUA_SCRIPT_DETAIL = """
function main(splash)
    splash.private_mode_enabled = false
    splash:go(splash.args.url)
    splash:wait(5)
    html = splash:html()
    splash.private_mode_enabled = true
    return html
end
"""

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

class TechbookfestUrlSpider(scrapy.Spider):
    name = 'techbookfest_url'
    allowed_domains = ['techbookfest.org']
    start_url = 'https://techbookfest.org/event/tbf10/market/newbook'

    def start_requests(self):
        yield scrapy_splash.SplashRequest(
            self.start_url,
            self.parse,
            headers={'User-Agent': USER_AGENT},
            endpoint='execute',
            args={'lua_source': LUA_SCRIPT_LIST},
        )

    def parse(self, response):
        for hrefs in response.css('div.r-bnwqim'):
            href = hrefs.css('a::attr(href)').extract_first()
            if href is not None:
                yield scrapy_splash.SplashRequest(
                    response.urljoin(href),
                    self.after_parse,
                    headers={'User-Agent': USER_AGENT},
                    endpoint='execute',
                    args={'lua_source': LUA_SCRIPT_DETAIL},
                )

    def after_parse(self, response):
        money_items = [''] * 4
        openning = ''

        for information in response.css('div.css-1dbjc4n div.r-18u37iz'):
            for h2_tag in information.css('div.css-1dbjc4n div.r-13awgt0 div.r-1jkjb'):
                title = h2_tag.css('h2::text').extract_first()
            for money_tag in information.css('div.css-18t94o4'):
                money = money_tag.css('div.css-901oao::text').extract()
                if len(money) == 0:
                    pass
                elif '電子版' in money[0]:
                    money_items[0] = ':'.join(money)
                elif '電子＋' in money[0]:
                    money_items[1] = ':'.join(money)
                elif '梅' in money[0]:
                    money_items[1] = ':'.join(money)
                elif '竹' in money[0]:
                    money_items[2] = ':'.join(money)
                elif '松' in money[0]:
                    money_items[3] = ':'.join(money)
            for event in information.css('div.css-1dbjc4n'):
                openning_tag = event.css('div.r-1enofrn::text').extract_first()
                if openning_tag is None:
                    pass
                elif '初出イベント' in openning_tag:
                    openning = openning_tag

        yield TechbookfestScrapyItem(
            title = title,
            money1 = money_items[0],
            money2 = money_items[1],
            money3 = money_items[2],
            money4 = money_items[3],
            openning = openning,
            url=response.url)
