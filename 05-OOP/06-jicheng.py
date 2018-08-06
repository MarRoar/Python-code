
'''
    继承
    语法
     class 类名称(父类名称,[父类名称])

     私有的方法和属性， 子类是不能直接用的
     可以用 dir(s) 来去查看
     print(s._Person__age) 私有属性的调用
'''

# 这是父类
class Person:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        #如果 age 是私有的呢
        self.__age = age # 私有的不可以

    def say_hello(self):
        print(self.name,  '的年龄是', self.__age)


class Student(Person):
    def __init__(self, name, age, sex):
        self.sex = sex

        # 体现不出继承了
        # self.name = name
        # self.age = age

        Person.__init__(self, name, age)
        # 构造函数中，包含调用父类构造函数，
        # 根据需要，不是必须得。子类不会自动调用父类的 __init__() 方法

s = Student('mar', 12, 'man')
s.say_hello()


# 可以打印查看类的层次
# Student -> Person -> Object
print('查看类的层次 ',Student.mro())


print(dir(s))
print(s._Person__age)
