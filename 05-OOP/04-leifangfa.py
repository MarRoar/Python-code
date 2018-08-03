'''
    类方法
    @classmethod

    静态方法
    @staticmethod

    类方法 和 静态方法是不能够调用 实例的属性和方法的
'''

class Studen:
    company = 'fpc'

    @classmethod
    def printCompany(cls):
        print(cls.company)
        # self 这里是 不可以调用的，原因看内存分析图

    @staticmethod
    def p():
        print('静态方法')
        # self 这里是 不可以调用的，原因看内存分析图

Studen.printCompany()