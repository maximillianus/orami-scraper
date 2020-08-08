# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OramiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class OramiLinkItem(scrapy.Item):
    category_level1 = scrapy.Field()
    category_level2 = scrapy.Field()
    category_level3 = scrapy.Field()
    url = scrapy.Field()
