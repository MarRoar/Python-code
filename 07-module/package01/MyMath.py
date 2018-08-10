'''
自定义一个模块
    实现数学四则运算
    两个数的加减乘除运算
'''
# 手动添加全局变量后 from MyMath import * 将不导入模块中的所有功能了，而是在列表中添加的了
# Python3 中 不提倡使用
# __all__ = ['add']

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == '__main__':

    a = 10
    b = 2

    print("和{0}".format(add(a, b)))
    print("差{0}".format(sub(a, b)))
    print("积{0}".format(mul(a, b)))
    print("商{0}".format(div(a, b)))

# __main__ 在当前执行的时候 这个变量是 __name__ = __main__
# print(__name__)