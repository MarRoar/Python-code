# 特殊方法 和 运算符的重载
# 就是运算符其实也是调用 Python的一些方法

class Person:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        ''' 重写了 + 的方法 '''
        if isinstance(other, Person):
            return("{0} ++++ {1}".format(self.name, other.name))
        else:
            print("不是同类对象，不能相加")

    def __mul__(self, other):
        return self.name * other

p1 = Person("mar")
p2 = Person("庖丁")

# 这样就重写了 + 的方法
c = p1 + p2
print(c)

# 重写了 * 的方法
c1 = p1 * 3
c2 = p2 * 3
print(c1)
print(c2)