'''
    全局变量和局部变量

    print(locals()) # 打印局部变量
    print(globals()) # 打印全局变量
'''
a = 100  #全局变量
b = 'out'
c = 'ccccccc'
def test1():
    global  a
    b = 20 # 局部变量, 出了这个函数就用不了了
    a = 300
    print(a)
    print(b)
    print('c=', c)

    print(locals()) # 打印局部变量
    print(globals()) # 打印全局变量

test1()
print(a)
print(b)