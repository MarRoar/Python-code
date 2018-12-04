# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os
import json
from scrapy import Request
from scrapy.exceptions import DropItem

class DoubanspiderPipeline(object):
	def __init__(self):
		self.filename = open('douban.json', 'w')

	def process_item(self, item, spider):
		text = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.filename.write(text.encode('utf-8'))

	def close_spider(self, spider):
		self.filename.close()


class ImagesPipeline(ImagesPipeline):


	IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

	def get_media_requests(self, item, info):
		image_url = item['posterLink']

		yield scrapy.Request(image_url)

	def item_completed(self, result, item, info):
		image_path = [x['path'] for ok, x in result if ok]

		if not image_path:
			raise DropItem('Image Downloaded Failed')
		return item
		
		# os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item['title'] + '.jpg')
		# item['posterPath'] = self.IMAGES_STORE + "/" + item['title']

		# return item

# class ImagePipeline(ImagesPipeline):
# 	def file_path(self, request, response=None, info=None):
# 		url = request.url
# 		file_name = url.split('/')[-1]
# 		return file_name

# 	def item_completed(self, results, item, info):
# 		image_paths = [x['path'] for ok, x in results if ok]
# 		if not image_paths:
# 			raise DropItem('Image Downloaded Failed')
# 		return item

# 	def get_media_requests(self, item, info):
# 		yield Request(item['posterLink'])