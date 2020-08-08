import scrapy

from ..items import OramiLinkItem

class OramiLinkSpider(scrapy.Spider):
    name = 'orami-links'
    start_urls = [
        'https://www.orami.co.id/',
        'https://www.orami.co.id/c/pakaian-bayi'
    ]

    def category_parser(self, node, next_level_selector):
        category_name = ''
        category_link = ''
        selector_lists = scrapy.selector.unified.SelectorList()
        elems = node.xpath('*')
        category_name = elems[0].css('a::text').get()
        category_link = elems[0].css('a::attr(href)').get()
        if len(elems) > 1:
            next_level_categories = elems[1]\
                    .css(next_level_selector)
            selector_lists = next_level_categories.xpath('li')
        return category_name, category_link, selector_lists

    def parse(self, response):
        level1_categories = response.css('#main-nav>li')
        # parse cat lv 1
        for cat in level1_categories[:]:
            NEXT_LEVEL_SELECTOR = '.second-level .wrap-second-cat>ul'
            level1_name, level1_link, level2_categories = \
                self.category_parser(cat, NEXT_LEVEL_SELECTOR)
            # parse cat lv 2
            for cat in level2_categories[:]:
                NEXT_LEVEL_SELECTOR = 'ul.wrap-third-cat.split-list'
                level2_name, level2_link, level3_categories = \
                    self.category_parser(cat, NEXT_LEVEL_SELECTOR)
                # parse cat lv 3
                for cat in level3_categories[:]:
                    NEXT_LEVEL_SELECTOR = 'none'
                    level3_name, level3_link, level4_categories = \
                        self.category_parser(cat, NEXT_LEVEL_SELECTOR)
                    yield OramiLinkItem(
                        category_level1=level1_name,
                        category_level2=level2_name,
                        category_level3=level3_name,
                        url=level3_link
                    )
