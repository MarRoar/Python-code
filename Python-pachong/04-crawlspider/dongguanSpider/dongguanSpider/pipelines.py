# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DongguanspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class DOnguangPipeline(object):
	def __init__(self):
		self.filename = open('news.json', 'w')

	def process_item(self, item, spider):
		text = json.dumps(dict(item), ensuer_ascii=False) + '\n'
		self.filename.write(text.encode('utf-8'))

	def close_item(self, spider):
		self.filename.close()
		