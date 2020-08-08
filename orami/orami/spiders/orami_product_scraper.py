import json
import scrapy
from pprint import pprint

from ..items import OramiProductItem

class OramiProductSpider(scrapy.Spider):
    name = 'orami-products'
    urlfilepath = './results/urls.json'
    try:
        with open(urlfilepath, 'r') as infile:
            urldata = json.load(infile)
        start_urls = [obj.get('url') for obj in urldata][:]
    except FileNotFoundError:
        # if no file found, set default urls
        start_urls = [
            'https://www.orami.co.id/c/pakaian-bayi',
        ]

    def get_category_names(self, response):
        categories = {}
        category_hierarchy = response.css('.breadcrumb>li')
        main = category_hierarchy[0].css('*::text').get()
        categories = {
            'level1': category_hierarchy[1].css('*::text').get(),
            'level2': category_hierarchy[2].css('*::text').get(),
            'level3': category_hierarchy[3].css('*::text').get(),
        }
        return categories
    
    def parse_product_details(self, product, categories):
        product_details = product.css('.wrap-widget-detail')
        product_name = product_details.css('.prod-name.mb-8 a::text').get()
        product_url = product.css('.prod-name.mb-8 a::attr(href)').get()
        product_brand = product_details.css('.prod-cat.mb-4 a::text').get()
        price_range = product_details.css('.price-range::text').get()
        normal_price = product_details.css('.normal-price::text, .price::text').get()
        disc_price = product_details.css('.disc-price::text').get()
        review_count = product_details.css('.total-review.color.is-txt.is-goblin.ml-8::text').get()
        rating = len(product_details.css('.fa.fa-star.fa-star.yellow:not(.fa-star-half-o)'))\
                 + (len(product_details.css('.fa.fa-star.fa-star-half-o.yellow')) * 0.5)

        # further data cleaning available in ItemPipeline
        return OramiProductItem(
            product_category_level1=categories['level1'],
            product_category_level2=categories['level2'],
            product_category_level3=categories['level3'],
            # product_name=product_name.strip() if product_name else None,
            # product_brand=product_brand.strip() if product_brand else None,
            # price_range=price_range.strip() if price_range else None,
            # normal_price=normal_price.strip() if normal_price else None,
            # disc_price=disc_price.strip() if disc_price else None,
            # is_onsale=True if disc_price else False,
            # review_count=review_count.strip() if review_count else '0',
            # rating=str(rating),
            product_name=product_name,
            product_brand=product_brand,
            price_range=price_range,
            normal_price=normal_price,
            disc_price=disc_price,
            is_onsale=True if disc_price else False,
            review_count=review_count.strip() if review_count else '0',
            rating=rating,
            product_url=product_url,
        )
    
    def get_next_page(self, response):
        CURRENT_PAGE_SELECTOR = '.pagination>.current>a::text'
        curr_page_num_str = response.css(CURRENT_PAGE_SELECTOR).get()
        try:
            curr_page_num = eval(curr_page_num_str)
        except:
            raise Exception('Page Number is not string')
        next_page_num_str = str(curr_page_num + 1)
        if '?page' not in response.url:
            next_page_url = f'{response.url}?page={next_page_num_str}'
        else:
            next_page_url = response.url\
                .replace(
                    f'?page={curr_page_num_str}',
                    f'?page={next_page_num_str}'
                )
        return next_page_url

    def parse(self, response):
        content_selector = '.tools-cat'
        content = response.css('.tools-cat')

        if not content:
            # if no content, end the scraping
            print('no content')
            return

        # get category level names
        categories = self.get_category_names(response)

        # get products
        PRODUCT_SELECTOR = '.prod-widget-vertical'
        products = response.css(PRODUCT_SELECTOR)
        for product in products[:]:
            yield self.parse_product_details(product, categories)

        # go to next page
        next_page_url = self.get_next_page(response)
        yield scrapy.Request(next_page_url, callback=self.parse)