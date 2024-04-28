from typing import Any
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Response

from items import JobinjaItem

class JobinjaSpider(scrapy.Spider):
    name = 'jobinja'
    start_urls = ['https://jobinja.ir/jobs/latest-job-post-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF']


    def parse(self, response: Response, **kwargs: Any) -> Any:
        self.logger.info(msg=f'\n\n start crawl {self.name} \n\n')
        
        works = response.xpath('//*[@id="js-jobSeekerSearchResult"]/div/div[3]/section/div/ul/li')
        for work in works:
            loader = ItemLoader(item=JobinjaItem(), selector=work)
            
            loader.add_value('provider',self.name)
            loader.add_xpath('title','div/div[1]/h2/a/text()')
            loader.add_xpath('link','div/div[1]/h2/a/@href')
            loader.add_xpath('cover','div/div[1]/a/img/@src')
            loader.add_xpath('company_name','div/div[1]/ul/li[1]/span/text()')
            loader.add_xpath('company_city','div/div[1]/ul/li[2]/span/text()')
            loader.add_xpath('type_cooperation','div/div[1]/ul/li[3]/span/span/text()')
            loader.add_value('date','today')
            loader.add_value('tags',[])
        

            yield loader.load_item()