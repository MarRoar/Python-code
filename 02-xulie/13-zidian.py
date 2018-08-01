'''
    字典添加，修改，删除
    1、直接给字典新增 键值对,如果有这个键的话会把之前的值给覆盖
        a['add'] = 'addVale'
    2、使用 update()
        a.update(b) 把 b 的 字典都添加到 a的字典上，如果有重复的则覆盖 a 的值
            a = {'name': 'paodn', 'age': 12}
            b = {'age': 22, 'sex': 'man'}
            a.update(b)
            print(a)
    3、删除
        del()
            del(a['name'])
        clear()
            删除所有
        pop()
            a.pop('name') 并且把 name 的值返回回来
    4、popitem() 随机删除 字典的键值对
        a.popitem()

'''

a = {'name': 'paodn', 'age': 12}
# b = {'age': 22, 'sex': 'man'}
# a.update(b)
# print(a)

# del a['age']
# b = a.pop('name')
# print(b)

b = a.popitem()
print(a)
print(b)