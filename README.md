# orami-scraper
Polite scraper for orami website. This scraper is based on Python's [Scrapy](https://docs.scrapy.org/en/latest/index.html) framework. This is my first time using Scrapy framework so I might not utilize all the best practices available for it.

## Scraper Objective
The objective of this scraper is to get all products information from Orami website.

## Application Flow
The scraper will first scrape the product categories' links and save it in `results/urls.json`. It will then scrape individual product information by looping through the urls and save them in `results/products.json` or `results/products.csv` whichever format you like.

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
   2. `./02_scrape_products.sh`
5. Results will be available in `results` directory.


