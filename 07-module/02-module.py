'''
模块的使用
    自定义模块
    导入模块
        1、import 模块名1, 模块名2 ...
            导入之后如何使用
                模块名.变量
                模块名.函数名(参数)
                模块名.类
        2、导入模块中相关的数据
            from 模块 import 变量，函数，类
            使用
                导入之后可以直接使用

'''

# 1、导入模块的方式
# import  random
# r = random.randint(1, 10)
# print(r)

#2、导入模块中相关数据的方式
from random import  randint
print(randint(1, 10))