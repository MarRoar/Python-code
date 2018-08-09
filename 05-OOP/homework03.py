'''
定义一个 Employee 雇员类，要求如下：

(1) 属性有：id、name、salary

(2) 运算符重载+：实现两个对象相加时，默认返回他们的薪水和

(3) 构造方法要求：输入 name、salary，不输入 id。id 采用自增的方式，从 1000 开始自增，第一个新增对象是 1001，第二个新增对象是 1002

(4) 根据 salary 属性，使用@property 设置属性的 get 和 set 方法。set 方法要求输入：1000-50000 范围的数
'''

class Employee:
    __id = 1000

    def __init__(self, name, salary):
        Employee.__id += 1

        self.id = Employee.__id
        self.name = name
        self.__salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.__salary + other.__salary
        else:
            return "只有同类对象才能相加"

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, value):
        if 1000 < value < 50000:
            self.__salary = value
        else:
            print("输入不符合要求")

a = Employee('1', 100)
b = Employee('2', 1000)

a.salary = 2000
ss = a + b
print(ss)




