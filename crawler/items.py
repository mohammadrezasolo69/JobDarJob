import scrapy
from itemloaders import processors

import re
import unicodedata

def clean_text(text):
    text = text.strip().replace('\u200c', ' ').replace('\n',' ')
    text = re.sub(r"<[^>]+>", "", text)
    text = unicodedata.normalize('NFKD', text)
    return text

# ------------------------------------------- Jobinja ------------------------------------------------
class JobinjaItem(scrapy.Item):
    provider = scrapy.Field(output_processor=processors.TakeFirst())
    title = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    link = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    cover = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    company_name = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    company_city = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    type_cooperation = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    date = scrapy.Field(input_processor=processors.MapCompose(clean_text),output_processor=processors.TakeFirst())
    tags = scrapy.Field()
