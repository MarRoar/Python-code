'''
    property 方法的使用
'''

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # 如果用修饰器来写的话

    # property 就相当于 getter 方法
    @property
    def salary(self):
        return self.__salary

    # 给 salary 设置 setter 方法
    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('请输入在1000--50000这个范围内')


    '''
    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('请输入在1000--50000这个范围内')
    def get_salary(self):
        return self.__salary
    '''

e1 = Employee('mar', 400)
'''
print(e1.get_salary())
e1.set_salary(20000)
print(e1.get_salary())
'''

# 用装饰器的写法来实现
print(e1.salary)
e1.salary = 2000
print(e1.salary)