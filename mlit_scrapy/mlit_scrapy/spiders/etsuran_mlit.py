import scrapy
from mlit_scrapy.items import MlitScrapyItem


class EtsuranMlitSpider(scrapy.Spider):
    name = 'etsuran_mlit'
    allowed_domains = ['etsuran.mlit.go.jp']
    start_urls = ['https://etsuran.mlit.go.jp/TAKKEN/chintaiKensaku.do']
    pref = '11'

    def __init__(self, pref='11', *args, **kwargs):
        super(EtsuranMlitSpider, self).__init__(*args, **kwargs)
        self.pref = pref

    def parse(self, response):
        return scrapy.FormRequest.from_response(
                    response,
                    formdata = dict(kenCode = self.pref
                    ,sortValue = '1', choice = '1'
                    ,dispCount = '50' ,CMD = 'search'),
                    callback = self.after_parse
                )

    def after_parse(self, response):
        for tr in response.css('tr'):
            if len(tr.css('td')) != 0:
                items = [''] * 6
                for index, td in enumerate(tr.css('td')):
                    items[ index ] = td.css('::text').extract_first()

                yield MlitScrapyItem(
                    licence = items[ 1 ],
                    company = items[ 2 ],
                    address = items[ 5 ]
                )

        tag = 'img[src="/TAKKEN/images/result_move_r.jpg"]::attr(onclick)'
        next_page = response.css(tag).extract_first()
        if next_page == '':
            return

        yield scrapy.FormRequest.from_response(
                    response,
                    formdata = dict(kenCode = self.pref
                    ,sortValue = '1', choice = '1'
                    ,dispCount = '50' ,CMD = 'next'),
                    callback = self.after_parse
                )
