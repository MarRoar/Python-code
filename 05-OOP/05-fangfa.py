'''
    实例方法的调用
'''

class Studen:

    def __init__(self, name, age):
        self.name = name #实例属性
        self.age = age

    def say_score(self): # 实例方法
        print(self.name, '的年级是', self.age)

s1 = Studen('mar', 18)

s1.say_score() # 实例方法可以这样调用

Studen.say_score(s1)

print(dir(s1))  #获得对象的属性和方法
print(s1.__dict__)  # 获得定义的属性
print(isinstance(s1, Studen)) # 对象是不是属于这个类的，是不是指定类型


# pass 空语句
class Man:
    pass


