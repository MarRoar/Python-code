# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['img3.doubanio.com']

    urls = 'https://img3.doubanio.com/view/photo/m/public/p480747492.webp'

    start_urls = [urls]

    def parse(self, response):

		item = DouyuspiderItem()

		item['nickName'] = 'shake'
		item['imageLink'] = urls

		yield item
