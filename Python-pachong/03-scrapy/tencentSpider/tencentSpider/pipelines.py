# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TencentspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

class TencentPipeline(object):
	def __init__(self):
		self.filename = open('tecent.json', 'w')

	def process_item(self, item, spider):
		textjson = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.filename.write(textjson.encode('utf-8'))

	def close_spider(self, spider):
		self.filename.close()

		
