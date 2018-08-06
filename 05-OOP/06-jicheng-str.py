'''
    继承
    重写 object 的 __str__() 方法
'''

class Person:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        '''重写 __str__ 方法'''
        return '重写了 str 方法'

p = Person('a')
print(p)




