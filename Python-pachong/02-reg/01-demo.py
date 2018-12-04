import urllib2
import re

class Spider:

	enable = True
	page = 1


	def loadPage(self, page):
		url = "http://www.neihan8.com/article/list_5_" + str(page)+ ".html"

		user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident / 5.0'

		headers = {'User-Agent': user_agent}

		req = urllib2.Request(url, headers=headers)

		response = urllib2.urlopen(req)

		html = response.read()

		gbk_html = html.decode('gbk').encode('utf-8')

		pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
		item_list = pattern.findall(gbk_html)

		return item_list

	def printOnePage(self, item_list, page):
		print '******  %d page load end'%page
		for item in item_list:
			# print '========'
			item = item.replace("<p>", '').replace("</p>", '').replace('<br />', '')
			self.writeToFile(item)
			# print item

	def writeToFile(self, text):
		myFile = open("./duanzi.txt", 'a')
		myFile.write(text)
		myFile.write("---------------------------------------------------------")
		myFile.close()

	def doWork(self):

		while self.enable:
			try:
				item_list = self.loadPage(self.page)
			except urllib2.URLError, e:
				print e.reason
				continue

			self.printOnePage(item_list, self.page)
			self.page += 1
			print "please enter ENTER continue"
			print 'quit back'

			command = raw_input()
			if (command == 'quit'):
				self.enable = False
				break


if __name__ == '__main__':

	mySpider = Spider()
	# item_list = mySpider.loadPage(1)
	# mySpider.printOnePage(item_list, 1)
	mySpider.doWork()




