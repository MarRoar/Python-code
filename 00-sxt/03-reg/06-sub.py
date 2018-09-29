'''
re 的高级用法
'''
import re

result = re.search(r"\d", 'asdf0')
print(result)

result = re.search(r"^\d$", 'asdf0')
print(result)


# search 只能找到一个
s = 'mar</h1>hellow od</h1>'
result = re.search(r'\w+</h1>', s)
print(result)

# findall 可以找到所有的
s = 'mar</h1>hellow lod</h1>'
result = re.findall(r'\w+</h1>', s)
print(result)

#sub 将匹配到的数据进行替换

# ret = re.sub(r"要替换的正则", '要替换的值', "要修改的字符串")


# 把 t 中的 php 都换成 python
t = "c++ php python shell window php python"
ret = re.sub(r"php", 'python', t)
print(ret)

print("---------------------------------------------------------------------------------")
# 现在要有目的的去替换
def replace(result):
    r = int(result.group()) + 20
    # 在原有的值上面加 20 
    return str(r)

ret = re.sub(r'\d+', replace, 'python = 100, php = 10')
print(ret)