'''
贪婪模式
'''
import re

s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)",s)
print(r.group(1))

s = "This is a number 234-235-22-423"
r = re.match("(.+)(\d+-\d+-\d+-\d+)",s) #前面的(.+) 是贪婪的，尽可能匹配多的
print(r.groups())

#在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
s = "This is a number 234-235-22-423"
r = re.match("(.+?)(\d+-\d+-\d+-\d+)",s) #前面的(.+) 是贪婪的，尽可能匹配多的
print(r.groups())

imgs = '''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'''
r = re.search(r"https.+?\.jpg", imgs) # 这个时候要关闭贪婪模式
print(r.group())


print("-----------------------------------------------------------")
# 练习题
# 把 http://www.interoem.com/messageinfo.asp?id=35  修改成 http://www.interoem.com/

s = 'http://www.interoem.com/messageinfo.asp?id=35'
result = re.sub(r'http://.+?/', '', s)
print(result)

result = re.sub(r'http://.+?/(.*)', '', s)
print(result)

result = re.sub(r'(http://.+?/).*', lambda x: x.group(1), s)
print(result)
# lambda 匿名函数表达式 ，和下面的一样

def replace(x):
    return x.group(1)
result = re.sub(r'(http://.+?/).*', replace, s)
print(result)
