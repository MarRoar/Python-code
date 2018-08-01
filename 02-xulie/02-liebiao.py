# -- coding: utf-8 --
'''
    列表
    列表：用于存储任意数目，任意类型的数据集合。
    列表是内置可变序列，是包含多个元素的有序连续的内存空间。

    列表中的元素可以是任意类型的

    列表的创建
    1、基本语法 [] 创建
    2、list() 创建
    3、range() 创建
    4、推导式生成列表
'''

a = ['hello', True]
b = [a, 't']
print(b)

c = list('list, create')
print(c)

print(list(range(10)))

d = [x*2 for x in range(10)]
print(d)