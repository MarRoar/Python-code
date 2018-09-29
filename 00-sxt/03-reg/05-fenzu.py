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
# \1 \2 提取的位置
result = re.match(r"<(.+)><(.+)>.+</\2></\1>", '<html><h1>helo world</h1></html>')
print(result)
result = re.match(r"<(.+)><(.+)>.+</\2></\1>", '<html><h1>helo world</h1></h1>')# 匹配不成功
print(result)


# 可以给 分组起名字 
result = re.match(r"<(?P<Key1>.+)><(?P<Key2>.+)>.+</(?P=Key2)></(?P=Key1)>", '<html><h1>helo world</h1></html>')
print(result)

# ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
# ret.group()



