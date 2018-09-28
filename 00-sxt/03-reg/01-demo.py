'''
正则
'''
import re

# result = re.match('正则表达式', '')

pattern = 'mar'
s = 'm'

result = re.match(pattern, s)
print(result)
print(dir(result))

r = 'mar'
result = re.match(pattern, r)
print(result)
print(result.group())

t = 'marui'
result = re.match(pattern, t)
print(result)
print(result.group())