import scrapy
import scrapy_splash
from techbookfest_scrapy.items import TechbookfestScrapyItem


LUA_SCRIPT = """
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

LUA_SCRIPT2 = """
function main(splash)
    splash.private_mode_enabled = false
    splash:go(splash.args.url)
    splash:wait(5)
    html = splash:html()
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
            args={'lua_source': LUA_SCRIPT},
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
                    args={'lua_source': LUA_SCRIPT2},
                )

    def after_parse(self, response):
        title = ''
        money = ''
        money1 = ''
        money2 = ''
        money3 = ''
        money4 = ''
        openning = ''

        for information in response.css('div.css-1dbjc4n div.r-18u37iz'):
            for ss in information.css('div.css-1dbjc4n div.r-13awgt0 div.r-1jkjb'):
                title = ss.css('h2::text').extract_first()
            for mm in information.css('div.css-18t94o4'):
                money = mm.css('div.css-901oao::text').extract()
                if len(money) == 0:
                    pass
                elif '電子版' in money[0]:
                    money1 = ':'.join(money)
                elif '電子＋' in money[0]:
                    money2 = ':'.join(money)
                elif '梅' in money[0]:
                    money2 = ':'.join(money)
                elif '竹' in money[0]:
                    money3 = ':'.join(money)
                elif '松' in money[0]:
                    money4 = ':'.join(money)
            for aaa in information.css('div.css-1dbjc4n'):
                vb = aaa.css('div.r-1enofrn::text').extract_first()
                if vb is None:
                    pass
                elif '初出イベント' in vb:
                    openning = vb


        yield TechbookfestScrapyItem(
            title = title,
            money1 = money1,
            money2 = money2,
            money3 = money3,
            money4 = money4,
            openning = openning,
            url=response.url)


# css-901oao r-1enofrn r-1byouvs r-rjixqe r-hrzydr

# <div role="button" data-focusable="true" tabindex="0" class="css-18t94o4 css-1dbjc4n r-1gvnnxv r-11u66rj r-z2wwpe r-rs99b7 r-t3h0cv r-1e081e0 r-5njf8e"><div dir="auto" class="css-901oao">電子版</div><div dir="auto" class="css-901oao">￥600</div></div>

# <div role="button" data-focusable="true" tabindex="0" class="css-18t94o4 css-1dbjc4n r-1gvnnxv r-11u66rj r-z2wwpe r-rs99b7 r-t3h0cv r-1e081e0 r-5njf8e"><div dir="auto" class="css-901oao">電子版</div><div dir="auto" class="css-901oao">￥500</div></div>