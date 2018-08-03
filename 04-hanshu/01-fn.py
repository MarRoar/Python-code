
'''
    Python函数的分类
        1、内置函数 str() len() 等
        2、标准库函数，
            我们通过 import 语句到入库，然后使用其中定义的函数比如 turtle 画图
        3、第三方库函数
            如科大讯飞的等等
        4、用户自定义函数

    函数定义
        def 函数名([参数]):
            """ 文档字符串(也就是函数的注释) """
            函数体

        函数也是对象，
        函数在定义和调用的时候参数的个数必须一致。

    形参和实参

'''

def test():
    ''' 这是一个测试的函数 '''
    print('hello world')

print(id(test))
print(type(test))
print(test)

# help(函数名.__doc__)
# 这个方法可以查看函数的 文档字符串
help(test.__doc__)

test()