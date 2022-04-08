# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    #在此处定义项目的字段 Field 定义字段
    #老师的姓名
    name = scrapy.Field()
    #老师的职称
    title = scrapy.Field()
    #老师信息
    info = scrapy.Field()

