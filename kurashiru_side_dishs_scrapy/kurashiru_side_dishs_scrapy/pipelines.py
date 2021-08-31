from itemadapter import ItemAdapter
from . database import session ,Base
from . recipe import Recipe


class KurashiruSideDishsScrapyPipeline:
    def process_item(self, item, spider):
        recipe = session.query(Recipe).filter(Recipe.site_url==item['site_url']).first()
        if recipe is None:
            recipes = Recipe()
            recipes.title = item['title']
            recipes.site_url = item['site_url']
            recipes.detail = item['detail']
            recipes.cooking_time = item['cooking_time']
            recipes.budget = item['budget']
            recipes.ingredient = item['ingredient']
            recipes.how_to_make = item['how_to_make']
            recipes.tip = item['tip']

            session.add(recipes)
            session.commit()

        return item
