'''
包的概念: package
    可以理解为文件夹，前提，文件包含一个 __init__.py
包的作用
    1、将模块归类，方便整理
    2、防止模块名冲突

包中的模块，名字会产生变化
    包名.模块名

包中的模块如何使用
    1、import 模块
    2、from 模块 imort 函数.
'''
# 1
# import MyMath
# import package01.MyMath

# 2
from package01.MyMath import *

print(add(1, 1))
