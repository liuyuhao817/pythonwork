import scrapy
from ..items import ItcastItem

class ITcastSpider(scrapy.Spider):
    #这个地方不用写__init__ 因为 只要写在parse函数外都属于初始化数据
    name = "itcast"  #必需参数 爬虫名称
    # allowed_domains 可选参数 表爬取域范围 运行爬虫在这个域名下进行爬取
    allowed_domains = ["http://www.itcast.cn"]
    # start_urls可迭代对象 源码中它拿到对象后就是先迭代它 然后取出每一个url地址
    #列表里的内容 爬虫执行后第一批请求 将从这个列表中获取
    # 初始URL元祖/列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  #必需参数

    # 解析response，并返回Item或Requests（需指定回调函数）
    # 当请求url返回网页没有指定回调函数时，默认的Request对象回调函数。
    # 用来处理网页返回的response，以及生成Item或者Request对象。
    def parse(self , response):
        not_list = response.xpath("//div[@class='li_txt']")

        #用来存储所有的item字段
        # items = []
        for node in not_list:
            #创建item字段对象 用于存储信息
            Item = ItcastItem()
            #.extract 将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            Item['name'] = name[0]
            Item["title"] = title[0]
            Item['info'] = info[0]

            # return Item
            # items.append(Item)
            #将获取到的数据提交给pipelines 即提交给管道文件处理 同时还回来继续执行后面的代码
            #yeild避免了将所有的Item存入items中占用大量内存的情况
            yield Item

        #此处是返回给引擎
        #yeild情况下 这里return返回数据 不经过pipelines
        # return items

            #打印出来的对象是在列表里
            # print(name[0])
            # print(title[0])
            # print(info[0])



