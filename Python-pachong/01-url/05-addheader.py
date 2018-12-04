import urllib2
import random

url ='http://www.baidu.com'

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]

user_agent = random.choice(ua_list)


header = {'User-Agent': user_agent}
request = urllib2.Request(url, headers=header)

request.add_header("Connection", "keep-live")

response = urllib2.urlopen(request)

print request.get_header("User-agent")
