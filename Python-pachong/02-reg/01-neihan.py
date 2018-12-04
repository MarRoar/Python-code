import urllib2
import re

class Spider:
    def __init__(self):
        self.page = 1
        self.switch = True
    
    def loadPage(self):
        print 'loadPage'
        url = "http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        
        html = response.read()
        gbk_html = html.decode('gbk').encode('utf-8')
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list = pattern.findall(gbk_html)
        self.dealPage(content_list)

    def dealPage(self, content_list):
        for item in content_list:
            item = item.replace('<br />', '').replace('<p>', '').replace('</p>', '')
            self.writePage(item)
    
    def writePage(self, item):
        with open('duanzi.txt', 'a') as f:
            f.write(item)

    def startWork(self):
        while self.switch:
            self.loadPage()
            command = raw_input('please enter continue, q back')
            if command == 'q':
                self.switch = False
            self.page += 1
        print '3q use'
	
if __name__ == '__main__':

    s = Spider()
    s.startWork()
