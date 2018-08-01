# -- coding: utf-8 ---

'''
    列表的添加和删除操作
    列表的添加和删除，如果数据量非常大的话，其实是非常消耗性能的，所以我们一般只是在列表的尾部添加和删除元素
    1、append()，对原来的列表进行修改
    2、+ 操作，这个操作会生成一个新的序列，
    3、extend(), 对原来序列进行修改
    4、insert(位置，值), 插入元素

    删除操作
    1、remove(值) 直接操作的是元素,首次出现的指定元素
    2、pop(index) 默认的删除最后一个值 index = -1 ,返回删除的值，对原来的序列进行操作。
    3、del 用法 del list[index] 删除 list中指定位置的值

    乘法扩展

'''

a = ['fir', 'ttt', True, 123]
# a.append(321)
# a.append(['hello', 'wolrd'])
# print(a)

# b = a + [20]
# print(a)
# print(b)

# a.extend('abc')
# a.extend(['321'])
# print(a)

# a.insert(20, False)
# print(a)

# a.remove('fir')
# print(a)

# b = a.pop(-2)
# print(b)
# print(a)

# del a[0]
# print(a)

# b = ['123', '456'] * 2
# print(b)