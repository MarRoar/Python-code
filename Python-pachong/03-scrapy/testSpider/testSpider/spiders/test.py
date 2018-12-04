# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu.com']

    url = 'http://www.baidu.com/'

    start_urls = [url]

    def parse(self, response):
        
        print response.url

        # if self.offset <= 30:
        # 	self.offset += 10
        # 	yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
