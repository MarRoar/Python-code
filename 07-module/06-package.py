'''
package
    模块
    __init__.py

    包中的__init__.py 初始化模块

    首次使用包中的模块的时候， __init__.py模块会被执行一次

__init__.py 中可以存放什么？
    可以存放普通模块一样的东西

一般会写一些辅助代码:

    在测试文件中
        import 包
    在__init__.py 中
        import 模块
    这种方式等价于：在测试问价中 import 包.模块
    --------------------------------------------------------

    在测试文件中
        from 包 import *
    在__init__.py 中
        from .模块 import *
    这种方式等价于：在测试问价中 from 包.模块 import *


'''
# import package01.MyMath

# import package01
# add = package01.MyMath.add
# print(add(1, 1))

from package01 import *
print(add(1, 1))