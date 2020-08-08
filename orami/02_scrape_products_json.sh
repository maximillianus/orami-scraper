#!/bin/bash

#variables
EXPORT_FILE=results/products.json

# start script
rm -f $EXPORT_FILE
scrapy crawl orami-products -o $EXPORT_FILE