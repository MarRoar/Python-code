# -- coding:utf-8 --
'''
    字典的创建
    1、a = {'name': 'paoding', 'age': 10}
    2、b = dict(name='paoding', age=10)
    3、b = dict([('name', 'paoding'), ('age', 10)])

    4、通过zip() 创建字典对象
        k = ['name', 'age]
        v = ['paoding', 12]
        d = dict(zip(k, v))
        print(d)
    5、通过fromkeys 来创建值为空None 的字典

'''

# k = ['name', 'age']
# v = ['paoding', 12]
# d = dict(zip(k, v))
# print(d)

a = dict.fromkeys(['name', 'age'])
print(a)