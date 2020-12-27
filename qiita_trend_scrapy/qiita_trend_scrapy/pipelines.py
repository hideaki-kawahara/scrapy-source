from itemadapter import ItemAdapter
from . database import session ,Base
from . tag import Tag


class QiitaTrendScrapyPipeline:
    def process_item(self, item, spider):
        tags = Tag()
        tags.keyword = item['keyword']
        tags.count = item['count']

        session.add(tags)
        session.commit()


        return item
