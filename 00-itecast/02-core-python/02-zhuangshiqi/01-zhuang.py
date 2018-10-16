'''
装饰器
'''

def w1(func):
    print("----------w1----------")
    def inner():
        print("inner")
        func()

    return inner

@w1
def f1():
    print("f1")

print("执行-------")
f1()


