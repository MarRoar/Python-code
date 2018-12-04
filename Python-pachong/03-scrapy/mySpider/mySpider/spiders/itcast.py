# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItecastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        items = []

        for each in response.xpath('//div[@class="li_txt"]'):
        	item = ItecastItem()

        	name = each.xpath("h3/text()").extract()
        	level = each.xpath("h4/text()").extract()
        	info = each.xpath("p/text()").extract()

        	item['name'] = name[0]
        	item['level'] = level[0]
        	item['info'] = info[0]


        	yield item
        	# items.append(item)

        # return items
