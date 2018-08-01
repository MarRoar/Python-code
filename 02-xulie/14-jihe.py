
'''
    集合
        集合底层是用字典来实现的，但是只有字典的键，

    使用 set() 将列表，元组等可迭代对象转成集合，如果有重复那么直保留一个

    remove(11) 删除指定的集合
    clear() 清空

    集合相关的操作
        并集，交集，差集

'''

a = {11, 20, 20, 30}
print(a)
a.add('hell')
print(a)

a.remove(11)
print(a)

a.clear()
print(a)





