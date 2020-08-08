import scrapy

class DownloadSpider(scrapy.Spider):
    name = 'downloader'
    start_urls = [
        'https://www.orami.co.id/',
        'https://www.orami.co.id/c/pakaian-bayi'
    ]

    def parse(self, response):
        page_name = response.url.split('/')[-1]
        if not page_name:
            page_name = 'main'
        page_name = page_name.replace('-', '_')
        with open(f'tests/html/orami_{page_name}_page.html', 'wb') as html_file:
            html_file.write(response.body)
