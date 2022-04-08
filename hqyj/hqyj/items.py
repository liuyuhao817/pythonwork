# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HqyjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #经验
    experience = scrapy.Field()
    #称号
    title = scrapy.Field()
