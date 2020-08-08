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

class OramiProductItem(scrapy.Item):
    product_category_level1 = scrapy.Field()
    product_category_level2 = scrapy.Field()
    product_category_level3 = scrapy.Field()
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    price_range = scrapy.Field()
    normal_price = scrapy.Field()
    disc_price = scrapy.Field()
    is_onsale = scrapy.Field()
    review_count = scrapy.Field()
    rating = scrapy.Field()
    product_url = scrapy.Field()
