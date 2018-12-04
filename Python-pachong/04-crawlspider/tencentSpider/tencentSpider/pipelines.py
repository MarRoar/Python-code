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
		self.filename = open('./tencent.json', 'w')

	def process_item(self, item, spider):
		jsontxt = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.filename.write(jsontxt.encode('utf-8'))

	def close_item(self, spider):
		self.filename.close()