'''
使用工厂模式、单例模式实现如下需求：

(1) 电脑工厂类 ComputerFactory 用于生产电脑 Computer。工厂类使用单例模式，也就是说只能有一个工厂对象。

(2) 工厂类中可以生产各种品牌的电脑：联想、华硕、神舟

(3) 各种品牌的电脑使用继承实现：

(4) 父类是 Computer 类，定义了 calculate 方法

(5) 各品牌电脑类需要重写父类的 calculate
'''

class ComputerFactory:
    __obj = None
    __init_flag = True

    def create(self, brand):
        if brand == '联想':
            return Lenove()
        elif brand == '华硕':
            return Asus()
        elif brand == '神舟':
            return Hasee()
        else:
            return '没有可生产的品牌'

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        if ComputerFactory.__init_flag:
            ComputerFactory.__init_flag = False

class Computer:
    def calculate(self):
        print("{0} calculate...".format(self))

class Lenove(Computer):
    '''联想电脑'''
    def calculate(self):
        print("{0} calculate...".format(self))

class Asus(Computer):
    '''华硕电脑'''
    def calculate(self):
        print("{0} calculate...".format(self))

class Hasee(Computer):
    '''神舟电脑'''
    def calculate(self):
        print("{0} calculate...".format(self))


computer = ComputerFactory()
l = computer.create("联想")
print(l)