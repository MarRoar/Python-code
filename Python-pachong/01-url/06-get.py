import urllib
import urllib2

url = "http://www.baidu.com"
word = {'wd': "beijing"}

word = urllib.urlencode(word)

newurl = url + "?" + word

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(newurl, headers=headers)

response = urllib2.urlopen(request)

print response.read()
