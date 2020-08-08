#!/bin/bash

 EXPORT_FILE=results/urls.json
 rm -f $EXPORT_FILE
 scrapy crawl orami-links -o $EXPORT_FILE