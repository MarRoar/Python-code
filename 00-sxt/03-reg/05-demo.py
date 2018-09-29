'''
正则
'''
import re
#正则表示 0 - 100
result = re.match(r"[1-9]\d?$|0|100", '0')
print(result)


result = re.match(r"[1-9]?\d?$|100", '0')
print(result)

result = re.match(r"<h1>(.*)</h1>", '<h1>helo world</h1>')
print(result.group(1))

result = re.match(r"(<h1>).*(</h1>)", '<h1>helo world</h1>')
print(result.group(1))
print(result.groups())

#<html><h1>helo world</h1></html>
result = re.match(r"<(.+)><(.+)>.+</\2></\1>", '<html><h1>helo world</h1></html>')
print(result)
result = re.match(r"<(.+)><(.+)>.+</\2></\1>", '<html><h1>helo world</h1></h1>')
print(result)



