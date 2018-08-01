# -- coding: utf-8 --
'''
    字典的访问
        a = {'name': 'paoding'}
        1、通过键获得值
            a['name'] => 得到值，如果这键不存在的话会报错
        2、通过get() 方法获得值。推荐使用，如果指定的键不存在的话，会返回None
        3、a.items() 列出所有的键值对
        4、列出所有的键，列出所有的值
            a.keys()
            a.value()
        5、len() 键值对的个数
        6、in 键值对是否在 字典中
'''
a = {'name': 'paoding', 'age': 18}
print(a['name'])
# print(a['salary']) # 这种情况会报错

print(a.get('name'))
print(a.get('salary'))
print(a.get('salary', 100))

print(a.items())

print(a.keys())
print(a.values())

print(len(a))
print('name' in a)