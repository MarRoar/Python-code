# -*- coding: utf-8 -*-

import scrapy
from dongguanSpider.items import DongguanspiderItem

class ScrapyDong(scrapy.Spider):
	name = 'scrapydong'

	allowed_domains = ['wz.sun0769.com']

	url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
	offset = 0
	start_urls = [url + str(offset)]

	print url + str(offset)
	def parse(self, response):

		print self.url + str(self.offset)

		if offset <= 250:
			self.offset += 30
			yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
