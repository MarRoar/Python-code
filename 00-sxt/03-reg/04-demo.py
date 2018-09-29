'''
正则
'''
import re
#转义
result = re.match('\\\\n\w', '\\nab')
print(result)

# 原始字符
s = r'\nabc'
print(s)

result = re.match(r'\\n\w', r'\nab')
print(result)

#边界
# ^ 开始
# $ 末尾 ， 其实在 vi 编辑器里面光标去头还是未也是这样的
print("--------------------------------------------")
result = re.match(r'^\w+\bve\b', 'hover')
print(result)

result = re.match(r'^\w+\bve\b', 'ho ve r')
print(result)
# \b 不能匹配空格
result = re.match(r'^\w+\sve\b', 'ho ve r')
print(result)

result = re.match(r'^.+ve\b', 'ho ve r')
print(result)