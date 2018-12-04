import urllib2

#httpproxy_handler = urllib2.ProxyHandler({"http": "111.230.183.90:8000"})

httpproxy_handler = urllib2.ProxyHandler({})

opener = urllib2.build_opener(httpproxy_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)

print response.read()
