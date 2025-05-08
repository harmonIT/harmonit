# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num=scrapy.Field()
    bl=scrapy.Field()
    name=scrapy.Field()
    status=scrapy.Field()
    day1=scrapy.Field()
    day2=scrapy.Field()
    link=scrapy.Field()
