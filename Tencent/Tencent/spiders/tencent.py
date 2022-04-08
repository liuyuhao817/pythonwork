import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    #爬虫名
    name = 'tencent'
    #爬虫爬取的数据域范围
    allowed_domains = ['tencent.com']
    #1、需要拼接的url
    baseURL = 'https://careers.tencent.com/jobopportunity.html='
    #1、需要拼接的url地址的偏移量
    offset = 0
    #爬虫启动时读取的url地址列表
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        #提取每个response数据
        note_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for note in note_list:
            #构建item对象 用来保存数据
            item = TencentItem()
            #提取到每个职位信息 并且将提取出的unicode字符串编码为utf8
            item["positionName"] = note.xpath("./td[1]/a/text()").extract()[0].encode('utf8')
            item["positionLink"] = note.xpath("./td[2]/a/@href").extract()[0].encode('utf8')
            if note.xpath("./td[3]/a/text()"):
                item["positionType"]= note.xpath("./td[3]/a/text()").extract()[0].encode('utf8')
            else:
                item["positionType"] = "NULL"
            item["peopleNumber"] = note.xpath("./td[4]/a/text()").extract()[0].encode('utf8')
            item["workLocation"] = note.xpath("./td[5]/a/text()").extract()[0].encode('utf8')
            item["publishTime"]= note.xpath("./td[6]/a/text()").extract()[0].encode('utf8')

            # yield重要性 要能返回数据 还能回来接着执行代码
            yield item

            # 第一种写法 拼接url 适用场景 页面没有点击的请求链接 必需通过拼接才能获取响应
            # if self.offset < 2190:
            #     self.offset += 10
            #     url = self.baseURL + str(self.offset)
            #     yield scrapy.Request(url,callback=self.parse)

            # 第二种写法 直接从response获取需要爬取的链接 并发送请求处理 直至链接全部提取完
            if not len(response.xpath("//a[@class='noactive' and @id='next']")):
                url = response.xpath("//a[@id='next']/@href").extract()[0]
                yield scrapy.Request(url, callback=self.parse)
