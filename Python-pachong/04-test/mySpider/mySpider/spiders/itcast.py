# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class ItecatSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/']
    start_urls = [
    	'http://www.itcast.cn/channel/teacher.shtml#ac'
    ]

    def parse(self, response):
        for each in response.xpath('//div[@class="li_txt"]'):

            item = MyspiderItem()

            item['name'] = each.xpath('./h3/text()').extract()[0]
            item['level'] = each.xpath('./h4/text()').extract()[0]
            item['desc'] = each.xpath('./p/text()').extract()[0]

            yield item
