import urllib
import urllib2

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

data = {
"i": "hello",
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
"salt": "1541485498748",
"sign": "a9755257db6737f62f00be5f1b4798e1",
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_REALTIME",
"typoResult": "false"
}

i_headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

d = urllib.urlencode(data)

request = urllib2.Request(url, data=d, headers=i_headers)
response = urllib2.urlopen(request)

print response.read()
