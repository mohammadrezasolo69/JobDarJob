import re
import unicodedata
import os

import scrapy
from itemloaders import processors


def clean_text(text):
    text = text.strip().replace('\u200c', ' ').replace('\n', ' ')
    text = re.sub(r"<[^>]+>", "", text)
    text = unicodedata.normalize('NFKD', text)
    return text

# ------------------------------------------- Jobinja ------------------------------------------------

def jobinja_clean_url(url):
    basename = os.path.basename(url)
    return url.replace(basename, '')


def jobinja_extract_slug_from_url(url):
    return url.split('/')[-2]


def jobinja_extract_url_cover(url):
    if "format(png)" in url:
        return url.split('filters:strip_exif():fill(transparent):format(png)/')[-1]

    elif "format(jpeg)" in url:
        return url.split('filters:strip_exif():fill(white):format(jpeg)/')[-1]
    else:
        return url


class JobinjaItem(scrapy.Item):
    provider = scrapy.Field(
        input_processor=processors.Identity(),
        output_processor=processors.TakeFirst()
    )

    slug = scrapy.Field(
        input_processor=processors.MapCompose(jobinja_extract_slug_from_url),
        output_processor=processors.TakeFirst()
    )

    title = scrapy.Field(
        input_processor=processors.MapCompose(clean_text),
        output_processor=processors.TakeFirst()
    )

    url_detail = scrapy.Field(
        input_processor=processors.MapCompose(jobinja_clean_url),
        output_processor=processors.TakeFirst()
    )

    cover = scrapy.Field(
        input_processor=processors.MapCompose(jobinja_extract_url_cover),
        output_processor=processors.TakeFirst()
    )

    company_name = scrapy.Field(
        input_processor=processors.MapCompose(clean_text),
        output_processor=processors.TakeFirst()
    )

    company_city = scrapy.Field(
        input_processor=processors.MapCompose(clean_text),
        output_processor=processors.TakeFirst()
    )

    type_cooperation = scrapy.Field(
        input_processor=processors.MapCompose(clean_text),
        output_processor=processors.TakeFirst()
    )

    # date = scrapy.Field()
    # tags = scrapy.Field()
