# 对象的 浅拷贝 和深拷贝

import copy

class Mobile:

    def __init__(self, cup, screen):
        self.cup = cup
        self.screen = screen

class Cpu:

    def calculate(self):
        print("计算")
        print("cup对象", self)

class Screen:

    def show(self):
        print("show")
        print("screen对象", self)

# 测试赋值
c1 = Cpu()
c2 = c1
print(c1)
print(c2)

print("浅拷贝")
# 测试浅拷贝
# m1 和 m2 不同，但是里面的 cup 和 screen 是相同的
s1 = Screen()
m1 = Mobile(c1, s1)
m2 = copy.copy(m1)
print(m1, m1.cup, m1.screen)
print(m2, m2.cup, m2.screen)

# 深拷贝
# 里面的每个对象都是不同的
print("深拷贝")
m3 = copy.deepcopy(m1)
print(m1, m1.cup, m1.screen)
print(m3, m3.cup, m3.screen)