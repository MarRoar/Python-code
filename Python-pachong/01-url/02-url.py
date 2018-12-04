import urllib2

request = urllib2.Request("http://wwww.baidu.com")

response = urllib2.urlopen(request)

print response.read()
