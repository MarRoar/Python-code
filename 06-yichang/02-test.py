
'''
异常的语法
try:
    可能会出现问题的语句
except 异常1:
except 异常2:
except 异常3:

如果所有的异常都没有捕获到的时候，就会报错

'''

# 异常的类型都有什么
'''
    1、ValueError: invalid literal for int() with base 10: 'a'
    2、ZeroDivisionError: division by zero
'''


a = input("请输入除数")
b = input("请输入被除数")

try:
    a = int(a)
    b = int(b)
    c = a / b
    print("商为%g"%c)
except ValueError:
    print("类型有误")
except ZeroDivisionError:
    print("除数不能为0")
