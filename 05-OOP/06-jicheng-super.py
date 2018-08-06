'''
 继承
 测试 super() 代表父类的定义，而不是父类的对象
'''

class A:
    def say(self):
        print('A', self)

class B(A):

    def say(self):
        # 如果重写的这个方法我就是想调用 A的 say() 方法呢
        # A.say(self)
        # 还可以使用 super
        super().say()
        print('B', self)

b = B()
b.say()