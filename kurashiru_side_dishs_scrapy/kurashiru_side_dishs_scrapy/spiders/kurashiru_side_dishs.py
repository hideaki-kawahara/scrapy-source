import scrapy
import re
from kurashiru_side_dishs_scrapy.items import KurashiruSideDishsScrapyItem

class KurashiruSideDishsSpider(scrapy.Spider):
    name = 'kurashiru_side_dishs'
    allowed_domains = ['www.kurashiru.com']
    start_urls = ['https://www.kurashiru.com/video_categories/243']

    def parse(self, response):
        for items in response.css('a.title'):
            detail_link = response.urljoin(items.css('a::attr(href)').extract_first())
            yield scrapy.Request(detail_link, callback=self.detail_parse)

        active_link = response.css('a.DlyLink-exact-active::attr(href)').extract_first()
        links = response.css('a.pagenate-button::attr(href)').extract()
        link_index = len(links)
        for i, link in enumerate(links):
            if active_link == link:
                if i + 1 < link_index:
                    yield scrapy.Request(response.urljoin(links[i + 1]), callback=self.parse)


    def detail_parse(self, response):
        ingredient_string = ''
        for ingredients in response.css('section.ingredients'):
            for ingredient in ingredients.css('li'):
                sub_title = ingredient.css('span.ingredient-title')
                if len(sub_title) != 0:
                    ingredient_string += sub_title.css('::text').extract_first() + '\n'
                else:
                    ingredient_string += (ingredient.css('a.ingredient-name::text').extract_first().strip()) + ' '
                    ingredient_string += ingredient.css('span.ingredient-quantity-amount::text').extract_first() + '\n'

        instruction_string = ''
        for instruction in response.css('li.instruction-list-item'):
            instruction_string += instruction.css('span.sort-order::text').extract_first() + ' '
            instruction_string += instruction.css('span.content::text').extract_first() + '\n'

        yield KurashiruSideDishsScrapyItem(
            site_url=response.url,
            title=response.css('h1.title::text').extract_first(),
            detail=response.css('p.introduction::text').extract_first(),
            cooking_time=(response.css('p.cooking-time::text').extract_first()).split('：'),
            budget=((response.css('p.expense::text').extract_first()).split('：')[1].strip()),
            ingredient=ingredient_string,
            how_to_make=instruction_string,
            tip=re.sub(r'\r\n|\r|\n', '\n', response.css('p.memo-content::text').extract_first())
        )







