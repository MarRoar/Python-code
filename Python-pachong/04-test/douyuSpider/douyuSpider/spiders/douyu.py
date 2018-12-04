# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0

    urls = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='

    start_urls = [urls + str(offset)]

    def parse(self, response):
    	data = json.loads(response.text)['data']

    	for each in data:
    		item = DouyuspiderItem()

    		item['nickName'] = each['nickname']
    		item['imageLink'] = each['vertical_src']

    		yield item

    	if self.offset <= 5:
    		self.offset += 1
    		yield scrapy.Request(self.urls + str(self.offset))
