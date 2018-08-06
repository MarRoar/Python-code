'''
    继承
    方法的重写
'''
# 这是父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print('我的年龄是', self.__age)
    def say_introduce(self):
        print('我的名字是', self.name)


class Student(Person):
    def __init__(self, name, age, sex):
        self.sex = sex
        Person.__init__(self, name, age)

    def say_introduce(self):
        '''重写 父类的这个方法'''

        print('报告，我的名字是', self.name)

s = Student('mar', 12, 'man')
s.say_age()
s.say_introduce()
