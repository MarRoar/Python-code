'''
    类属性

    一一个类，只有一个类对象，也就是在堆内只有一份
'''

class Studen:
    company = 'fpc' # 类属性
    count = 0  # 类属性

    def __init__(self, name, age):
        self.name = name #实例属性
        self.age = age
        Studen.count = Studen.count + 1

    def say_score(self): # 实例方法
        print('我的公司是{0}'.format(Studen.company))
        print(self.name, '的年级是', self.age)

s1 = Studen('mar', 18)
s2 = Studen('mar', 180)

s1.say_score()
print(Studen.count) # 可以查看实例化的多少次

