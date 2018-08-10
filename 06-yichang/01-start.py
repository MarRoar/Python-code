
'''
# 异常： Python解释器遇到无法解释的代码的时候，罢工

异常的语法
try:
    可能会出现问题的语句
except:
    # 出错后的操作

'''

a = input("请输入除数")
b = input("请输入被除数")

try:
    a = int(a)
    b = int(b)
    c = a / b
    print("商为%g"%c)
except:
    print("输入有误/除数不能为0")
