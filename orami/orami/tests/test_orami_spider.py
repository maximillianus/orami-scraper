import unittest
from orami.spiders import orami_link_scraper, orami_product_scraper
from scrapy.http import HtmlResponse

class OramiSpiderTest(unittest.TestCase):

    def setUp(self):
        self.link_spider = orami_link_scraper.OramiLinkSpider()
        self.product_spider = orami_product_scraper.OramiProductSpider()
        fake_url = 'http://www.example.com'
        with open('orami/tests/html/orami_main_page.html', 'r') as html_file:
            self.main_page_html = HtmlResponse(
                url='https://www.orami.co.id/',
                encoding='utf8',
                body=html_file.read()
            )
        with open('orami/tests/html/orami_pakaian_bayi_page.html', 'r') as html_file:
            self.pakaian_bayi_html = HtmlResponse(
                url='https://www.orami.co.id/c/pakaian-bayi',
                body=html_file.read(),
                encoding='utf8'
            )

    def test_parse_link(self):
        expected_result = 237
        result_generator = self.link_spider.parse(self.main_page_html)
        results = [r for r in result_generator]
        self.assertEqual(expected_result, len(results))

    def test_parse_products(self):
        expected_result = 41
        result_generator = self.product_spider.parse(self.pakaian_bayi_html)
        results = [r for r in result_generator]
        self.assertEqual(expected_result, len(results))


if __name__ == "__main__":
    unittest.main()