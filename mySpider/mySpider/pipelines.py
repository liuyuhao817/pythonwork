# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#管道作用：处理item字段

import json

class MyspiderPipeline(object):
    def __init__(self):
        # 可选实现，做参数初始化等
        # doing something
        self.f = open("itcast_pippeline.json","wb")

    def process_item(self, item, spider):
        """
        :param item: 被爬取的item
        :param spider: 爬取该item的spider
        这个方法必须实现，每个item pipeline组件都需要调用该方法，
        这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理
        """
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.f.write(content.encode("utf8"))
        #此处返还给引擎
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用
        pass


    #爬虫退出时执行的函数
    # spider (Spider 对象) – 被关闭的spider
    # 可选实现，当spider被关闭时，这个方法被调用
    def close_spider(self,spider):
        self.f.close()


