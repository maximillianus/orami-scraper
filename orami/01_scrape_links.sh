#!/bin/bash

# variables
EXPORT_FILE=results/urls.json

# start script
rm -f $EXPORT_FILE
scrapy crawl orami-links -o $EXPORT_FILE