'''
正则
数量
'''
import re

result = re.match('\d*', '')
print(result)

result = re.match('\d*', 'adsf')
print(result)

result = re.match('\d*', '123asd')
print(result)

result = re.match('\d+', '')
print(result)

print("---------------------------------=---------------")

result = re.match('\d+[a-z]', '123asdf')
print(result)

result = re.match('\d*[a-z]', '123asdf')
print(result)

result = re.match('\d?[a-z]', '123asdf')
print(result)
