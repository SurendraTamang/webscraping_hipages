#### Extracting hipages with Scrapy
In this project, I scraped some useful data from the site
[Hipages website](https://hipages.com.au/) one of the australian websites
using simple.

I used the proxies for dealing with limited request blockage.We need to
add the proxies.txt file on the path where scrapy.cfg is present


### How to run the  scrapy

    scrapy crawl hipages_spider -o hipages_data.csv

I have checked in required csv file of this spider.