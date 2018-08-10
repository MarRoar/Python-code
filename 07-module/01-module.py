'''
    什么是模块？
        只要以 .py 为后缀的文件，都可以被称为模块
    模块中可以包含什么东西
        1、变量
        2、函数
        3、class 面向对象（类 -》 对象）
        4、可执行代码

    使用模块的好处?
        管理方便，易维护
        降低复杂度
'''

PI = 3.14

def get_area(r):
    '''
    求圆的面积
    :param r:
    :return:
    '''
    return PI * r ** 2

class Student:
    pass


print(PI)