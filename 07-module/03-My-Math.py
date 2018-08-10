'''
使用自定义模块
    1、import 模块
        问题：在导入模块的时候，模块里面的代码会执行一遍
        解决办法:
            在自定义模块中使用 __name__ 变量来判断
            if __name__ == '__main__':
                测试代码块
    2、from 模块 import 函数
'''

# 1、
# import MyMath
#
# a = 45
# b = 10
#
# print(MyMath.add(a, b))

# 2、
from MyMath import add, sub
a = 101
b = 2
print(add(a, b))