# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguanSpider.items import DongguanspiderItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    page_lx = LinkExtractor(allow=r'type=4')
    contentlink = LinkExtractor(allow=r'html/question/\d+/\d+.html')

    rules = (
        Rule(page_lx, process_links="deal_links"),
        Rule(contentlink, callback='parse_item'),
    )

    def deal_links(self, links):
        for each in links:
            each.url = each.url.replace("?", '&').replace("Type&", "Type?")

        return links

    def parse_item(self, response):

        item = DongguanspiderItem

        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()')

        # print item['title']

        item['number'] = item['title'].split(' ')[2].split(':')[1]

        item['content'] = response.xpath('//div[@class="pagecenter p3"]//div[@class="c1 text14_2"]/text()]')

        item['url'] = response.url

        yield item
