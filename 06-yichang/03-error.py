
'''
异常铺货不到的,
这个错误就会给Python解释器
所以就报错了


多个异常的顺序，在前面的先会执行
所以说，子类在前，父类在后
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
except IOError: # 我在这里修改了异常
    print("IOError")
except ZeroDivisionError: # 按着ctrl + 双击 ZeroDivisionError 可以查看定义的位置
    print("除数不能为0")
except Exception:
    # 这个异常的作用是，这个是父类的异常，
    # 所有的异常都会捕获
    print("其他异常")
