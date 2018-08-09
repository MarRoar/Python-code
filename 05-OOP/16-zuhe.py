# 组合 和继承

class A1:

    def say_a1(self):
        print("a1,a1")

class B1(A1):
    pass

# 在这个 b 要用 a 的 say_a1() 方法
# 这里是使用继承来实现的
b1 = B1()
b1.say_a1()


class A2:

    def say_a2(self):
        print("a2,a2")

class B2:

    def __init__(self, a):
        self.a = a

# 用组合的方式实现代码复用
a2 = A2()
b2 = B2(a2)
b2.a.say_a2()
