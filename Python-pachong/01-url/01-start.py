
import urllib2

response = urllib2.urlopen("http://www.baidu.com")

print response.read()



# import urllib2

# try:
# 	response = urllib2.urlopen("http://www.baidu.com")
# 	print response.read()
# except urllib2.URLError, e:
# 	print e.reason