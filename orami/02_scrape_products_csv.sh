#!/bin/bash

# variables
EXPORT_FILE=results/products.json
EXPORT_FILE_CSV=results/products.csv

# start script
rm -f $EXPORT_FILE
# scrapy produces unordered csv so I am doing a convert on my own
# scrapy crawl orami-products -t csv -o $EXPORT_FILE
scrapy crawl orami-products -o $EXPORT_FILE
python3 utils/jsontocsv.py -i $EXPORT_FILE -o $EXPORT_FILE_CSV