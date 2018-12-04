import urllib2

url ='http://www.baidu.com'

header = {'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib2.Request(url, headers=header)

request.add_header("Connection", "keep-live")

response = urllib2.urlopen(request)

print response.read()
print response.code
