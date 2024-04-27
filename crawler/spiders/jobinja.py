from typing import Any
import scrapy
from scrapy.http import Response

class JobinjaSpider(scrapy.Spider):
    name = 'jobinja'
    start_urls = ['https://jobinja.ir/jobs/latest-job-post-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF']


    def parse(self, response: Response, **kwargs: Any) -> Any:
        yield {'url':response.url}