import scrapy


class HqyjtSpider(scrapy.Spider):
    name = 'hqyjt'
    allowed_domains = ['http://www.hqyj.com/']
    start_urls = ['http://www.hqyj.com/teachers/']

    def parse(self, response):
        not_list = response.xpath("//div[@class='g-t-list']")
        for node in not_list:
            Item = HqyjtSpider()
            name = node.xpath("./div/p/text()").extract()[0].encode('utf8')
            experience = node.xpath("./div/em/text()").extract()[0].encode('utf8')
            title = node.xpath("./div/span/text()").extract()[0].encode('utf8')
            Item['name'] = name
            Item['experience'] = experience
            Item['title'] = title

            yield Item