from db.conection import connect_to_db
from pprint import pprint
from db.models import JobPosition


class ImdbPipelineSingle:

    def process_item(self, item, spider):
        connect_to_db()

        print('******************************************************')
        pprint(item)
        print('******************************************************')

        JobPosition(
            provider=item['provider'],
            title=item['title'],
            url_detail=item['url_detail'],
            cover=item['cover'],
            company_name=item['company_name'],
            company_city=item['company_city'],
            type_cooperation=item['type_cooperation'],
            # date=item['date'],
            slug=item['slug'],
        ).save()

        return item
