# coding:utf-8 ---

'''
    元组的创建
    1、() 创建
    2、tuple() 创建

    tuple() 可以接收列表、字符串、其他序列类型、迭代器生成元组
    list() 可以接收元组、字符串、其他序列类型、迭代器生成列表

'''
a = (1, 2, 3, 4, 5)
print(a)
#也可以把() 这个括号省略
b = 1, 2, 3, 4, 5
print(b)

c = tuple('abcdef')
print(c)
d1 = [1, 2, 3]
d = tuple(d1) # 把一个列表创建成元组
print(d)

e1 = range(5)
e = tuple(e1)
print(e)