import time
from datetime import datetime
from typing import Any
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Response
from scrapy.signals import spider_closed

from crawler.items import JobinjaItem


class JobinjaSpider(scrapy.Spider):
    name = 'jobinja'
    last_slug = None
    start_urls = [
        "https://jobinja.ir/jobs/latest-job-post-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF?sort_by=published_at_desc" + f'&page={page_number}'
        for page_number in range(1, 2)
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        self.logger.info(msg=f'\n\n start crawl {self.name} \n\n')

        works = response.xpath('//*[@id="js-jobSeekerSearchResult"]/div/div[3]/section/div/ul/li')
        for number, work in enumerate(works):
            loader = ItemLoader(item=JobinjaItem(), selector=work)

            loader.add_value('provider', self.name)
            loader.add_xpath('slug', 'div/div[1]/h2/a/@href')
            loader.add_xpath('title', 'div/div[1]/h2/a/text()')
            loader.add_xpath('url_detail', 'div/div[1]/h2/a/@href')
            loader.add_xpath('cover', 'div/div[1]/a/img/@src')
            loader.add_xpath('company_name', 'div/div[1]/ul/li[1]/span/text()')
            loader.add_xpath('company_city', 'div/div[1]/ul/li[2]/span/text()')
            loader.add_xpath('type_cooperation', 'div/div[1]/ul/li[3]/span/span/text()')

            loader.add_value('date', datetime.now())
            # loader.add_value('tags',[])

            if self.last_slug is None and number == 0:
                self.last_slug = work.xpath('div/div[1]/h2/a/@href').get().split('/')[-2]

            yield loader.load_item()
