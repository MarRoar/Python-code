# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = [
        'movie.douban.com',
        'img1.doubanio.com',
        'img3.doubanio.com']

    offset = 0
    urls = 'https://movie.douban.com/top250?filter=&start='
    start_urls = [urls + str(offset)]

    def parse(self, response):

    	for each in response.xpath('//div[@id="content"]//div[@class="article"]//ol//div[@class="item"]'):
    		item = DoubanspiderItem()

    		item['title'] = each.xpath('.//div[@class="info"]//div[@class="hd"]//span[1]/text()').extract()[0]

    		item['posterLink'] = each.xpath('.//div[@class="pic"]//img/@src').extract()[0]

    		# item['bd'] = each.xpath('.//div[@class="info"]//div[@class="bd"]/p/text()').extract()[0]

    		# item['star'] = each.xpath('.//div[@class="info"]//div[@class="bd"]//div[@class="star"]//span[@class="rating_num"]/text()').extract()[0]

    		# quote = each.xpath('.//div[@class="info"]//div[@class="bd"]//p[@class="quote"]//span/text()').extract()

            # if len(quote) != 0:
            #     item['quote'] = quote[0]

    		yield item

    	if self.offset < 25:
    		self.offset += 25

    		yield scrapy.Request(self.urls + str(self.offset), callback=self.parse)