'''
    使用自定义模块的时候
    1、import 模块
    2、from 模块 import 函数
        使用这种方式导入模块中的功能，一个一个写，如果这里面的方法比较多的话，就比较麻烦
        解决办法是
            from 模块 import *

        * 默认是导入模块中的所有功能
        如果在模块中手动添加全局变量 __all__ = []
'''

from MyMath import *
a = 10
b = 5
print(add(a, b))
print(sub(a, b))

