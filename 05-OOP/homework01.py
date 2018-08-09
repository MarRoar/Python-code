'''
设计一个名为 MyRectangle 的矩形类来表示矩形。这个类包含
(1) 左上角顶点的坐标：x，y
(2) 宽度和高度：width、height
(3) 构造方法：传入 x，y，width，height。如果（x，y）不传则默认是 0，如果 width和 height 不传，则默认是 100.
(4) 定义一个 getArea() 计算面积的方法
(5) 定义一个 getPerimeter()，计算周长的方法
(6) 定义一个 draw()方法，使用海龟绘图绘制出这个
'''

import turtle
class MyRectangle:
    '''
        一个矩形类
        1、属性有 左上角左边x, y。 矩形的宽高 width、height
        2、方法有 getArea()、getPerimeter()、draw()
    '''
    def __init__(self, x = 0, y = 0, width = 100, height = 100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        '''计算矩形面积'''
        return self.width * self.height / 2

    def getPerimeter(self):
        '''计算矩形周长'''
        return (self.width + self.height) * 2

    def draw(self):
        '''绘制这个矩形'''
        t = turtle.Pen()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)

        turtle.done()

m = MyRectangle(50, -50, 120, 80)
m.draw()