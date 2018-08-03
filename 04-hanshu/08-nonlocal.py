'''
    关键字 nonlocal

    和 global 比较类似
'''
a = 100
def outer():
    b = 20
    def inner():
        # print(b) 这里会报错的
        nonlocal b #如果要修改 b 的话 必须先声明一下 b
        print(b)
        b = 30

        global  a # 就知道是全局的变量了
    inner()
    print('outer b =', b)

outer()
