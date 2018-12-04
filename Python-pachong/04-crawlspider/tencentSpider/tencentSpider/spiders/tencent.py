# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentSpider.items import TencentspiderItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    page_li = LinkExtractor(allow=r'start=\d+')

    rules = [
        Rule(page_li, callback='parse_item', follow=True)
    ]
    

    def parse_item(self, response):

        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()

            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]

            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]

            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]

            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]

            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item