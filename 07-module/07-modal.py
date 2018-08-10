'''
1、模块的发布
    a. 为什么发布
        在定义模块在新项目中不能用
    b. sys.path
        导入模块时，搜索路基列表
        如果所有路径中都没有要导入的模块，会导致无法导入目标模块

    解决方案
        1、将模块所在路径，手动加入到sys.path 列表中
            在要使用的项目里面手动的 加入package_file = "F:\\MarLen\\Python\\Python-code\\07-module"
            sys.path.append(路径)
            然后引入模块

        2、将自定义模块，发布到系统目录
            发布自定义模块的步骤
            1、确定的发布的模块(目录结构)
                |-- setup.py
                |-- package01
                    |
                    -- 自定义模块 MyMath
            2、setup的编辑工作
                setup()
            3、构建模块
                python setup.py build
            4、发布模块
                python setup.py sdist

2、模块的安装
    2.1 通过命令完成安装
        - 安装的方式
            - 找到模块的压缩包
            - 解压
        - 进入文件夹
        - 执行命令 python setup.py install

    2.2 暴力安装
        直接将包复制到site-packages

'''

import sys
list1 = sys.path
for path in list1:
    print(path)
