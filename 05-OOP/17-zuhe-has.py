# has-a 的组合关系
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

m = Mobile(Cpu(), Screen())
m.cup.calculate()
m.screen.show()