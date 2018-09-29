import re

ret = re.match(".", "M")
print(ret.group())

p = "1[345]" # 这个正则也就是匹配13、14、15 这三种情况
result1 = re.match(p, '12') #不匹配
print(result1)
result2 = re.match(p, '13') # 匹配
print(result2)

rP = "1[^345]" # [] 里面有个 ^ 表示取反的意思也就是不是这三个数的情况
result1 = re.match(rP, '12') #匹配
print(result1)
result2 = re.match(rP, '13') #不匹配
print(result2)

print("----------------------------------------------")

result = re.match('\d', "13") # 数字
print(result)

result = re.match("嫦娥\d号","嫦娥3号发射成功")
print(result)

