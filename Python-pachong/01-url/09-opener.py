import urllib2

http_handler = urllib2.HTTPHandler()

opener = urllib2.build_opener(http_handler)

request = urllib2.Request('http://wwww.baidu.com/')

response = opener.open(request)

print response.read()
