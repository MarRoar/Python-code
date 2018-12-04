# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban_img'
    allowed_domains = [
        'movie.douban.com',
        'img1.doubanio.com',
        'img3.doubanio.com']

    offset = 0
    urls = 'https://movie.douban.com/top250?filter=&start='
    start_urls = [urls + str(offset)]

    def parse(self, response):
        item = DoubanspiderItem()

        item['posterLink'] =  'https://img3.doubanio.com/view/photo/m/public/p480747492.webp'
        yield item        
