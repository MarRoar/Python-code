'''
装饰器原理
'''

def w1(fn):
    def inner():
        print("验证中---")
        fn()

    return inner

def f1():
    print("f1")

f1 = w1(f1)
f1()