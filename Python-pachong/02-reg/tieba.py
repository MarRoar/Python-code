import os
import urllib
import urllib2
from lxml import etree

class Spider:
    def __init__(self):
        self.tiebaName = raw_input('tieba:')
        self.beginPage = int(raw_input('begin page:'))
        self.endPage = int(raw_input('end page:'))

        self.url = 'http://tieba.baidu.com/f'
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        self.userName = 1

    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50
            word = {'pn': pn, 'kw': self.tiebaName}
            
            word = urllib.urlencode(word)
            myUrl = self.url + '?' + word
            self.loadPage(myUrl)            

    def loadPage(self, url):
        request = urllib2.Request(url, headers=self.ua_header)
        html = urllib2.urlopen(request).read()

        selector = etree.HTML(html)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link = 'http://tieba.baidu.com' + link
            self.loadImages(link)

    def loadImages(self, url):
        req = urllib2.Request(url, headers=self.ua_header)
        html = urllib2.urlopen(req).read()

        selector = etree.HTML(html)
        imageLInks = selector.xpath('//img[@class="BDE_Image"]/@src')

        for imagesLink in imageLInks:
            self.writeImages(imagesLink)

    def writeImages(self, img):
        print 'now copy image file ...'

        file = open('./imgs/' + str(self.userName) + '.png', 'wb')

        images = urllib2.urlopen(img).read()

        file.write(images)
        file.close()

        self.userName += 1
    
    

if __name__ == '__main__':
    s = Spider()
    s.tiebaSpider()
