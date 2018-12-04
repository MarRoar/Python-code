# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class MyspiderPipeline(object):

	def __init__(self):
		self.filename = open('teacher.json', 'w')

	def process_item(self, item, spider):
		text = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.filename.write(text.encode('utf-8'))

	def close_spider(self, spider):
		self.filename.close()