from datetime import datetime

from db.conection import connect_to_db
from pprint import pprint
from db.models import JobPosition, Provider


class JoninjaPipeline:

    def open_spider(self, spider):
        connect_to_db()

    def process_item(self, item, spider):
        provider = Provider.objects.filter(slug=item['provider']).first()

        if item['slug'] != provider.last_slug:
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

        provider.update(last_slug=item['slug'], run_date=datetime.now())

        return item
