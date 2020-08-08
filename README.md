# orami-scraper
Polite scraper for [Orami](https://www.orami.co.id/) website. 

This scraper is based on Python's [Scrapy](https://docs.scrapy.org/en/latest/index.html) framework. This is my first time using Scrapy framework so I might not utilize all the best practices available for it.

## Scraper Objective
The objective of this scraper is to get all products information from [Orami](https://www.orami.co.id/).website.

## Application Details

### Flow
The scraper will first scrape the product categories' links and save it in `orami/results/urls.json`. It will then scrape individual product information by looping through the urls and save them in `orami/results/products.json` or `orami/results/products.csv` whichever format you like.

Sample results are also available `orami/results/`

### Output Format
Scrapy has a native CSV Exporter however I don't use it since it produces unordered columns in the result. There are ways to modify scrapy to work around this but it is much simpler to create my own `json-to-csv` converter in `utils/jsontocsv.py` to do the format conversion.

### Settings
In order to be more polite to the website, I have set up throttling to the crawler. This includes increasing delay between downloads and lowering number of concurrent requests. You can adjust these settings if you want a faster crawling but it is recommended to keep it at reasonable rate to avoid stress on the website.

### Unit Test
Run the unit test from the project directory ie. `orami-scraper/orami`.

Run it using: `python3 -m unittest orami.tests.test_orami_spider`
OR
Run it using the shellscript: `./03_run_unittest.sh`


### Other Notes
- skipped on linting but you can use `black` or `flake8` if you wish to have it
- again, remember to scrape politely

## Getting it up and running
1. Ensure you have Python 3
   - `brew install python3` if you are using Mac
   - `sudo apt-get install python3` if you are using Ubuntu Linux
   - download and install from [Official Python Website](https://www.python.org/) if you are on Windows
2. Install and activate virtual environment
   - `virtualenv venv`
   - `source venv/bin/activate`
3. Install scrapy
   - `pip install scrapy`
4. Go to `orami` directory and run the shellscripts
   1. `./01_scrape_links.sh`
   2. `./02_scrape_products_json.sh` for json output or `./02_scrape_products_csv.sh` for csv
5. Results will be available in `results` directory.


