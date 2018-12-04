# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import Doubanimg2Item

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        
        item = Doubanimg2Item()
        sel = Selector(response)

        images = sel.xpath('//*[@id="content"]/div/div[1]/ol/li')

        item['url'] = []
        item['img_name'] = []

        for image in images:
        	site = image.xpath('div/div[1]/a/img/@src').extract_first()
        	img_name = image.xpath('div/div[1]/a/img/@alt').extract_first()

        	item['url'].append(site)
        	item['img_name'].append(img_name)

        yield item
