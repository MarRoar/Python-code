# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    base_url = 'https://hr.tencent.com/'

    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='+ str(offset)

    start_urls = [url]

    def parse(self, response):
    	for each in response.xpath('//tr[@class="event"] | //tr[@class="odd"]'):
    		item = TencentspiderItem()

    		item['positionName'] = each.xpath('./td/a/text()').extract()[0]

    		item['positionLink'] = self.base_url + each.xpath('./td/a/@href').extract()[0]

    		item['positionType'] = each.xpath('./td[2]/text()').extract()[0]

    		item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]

    		yield scrapy.Request(item['positionLink'], meta = {'item': item}, callback=self.parse_desc)

    	if self.offset <= 60:
    		self.offset += 10
    		yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_desc(self, response):
    	item = response.meta['item']
    	desc = ''
    	for each in response.xpath('//div[@class="lightblue"]/text()').extract():
    		desc += each

    	item['positionDesc'] = desc

    	yield item