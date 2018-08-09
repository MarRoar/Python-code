# 使用海龟绘图。输入多个点，将这些点都两两相连。

'''

'''

import  turtle
turtle.speed(1)
t = turtle.Pen()

def drawLine():
    s = input('输入坐标,(如 (x1,y1), (x2,y2)), ... : ')
    s =eval(s)
    l = len(s)

    # 双层遍历去画线
    for i in range(l):
        # 取出第一个点
        item1 = s[i]
        x1, y1 = item1[0], item1[1]

        for j in range(i+1, l):
            # 取出除第一个点之外的点，然后连接
            item2 = s[j]
            x2, y2 = item2[0], item2[1]
            t.goto(x2, y2)

            t.goto(x1, y1)
    turtle.done()

drawLine()

# (100, 100), (100, -100), (-100, -100), (-100, 100)
# t.goto(1, 2)
# t.goto(50, 10)
# t.goto(-10, -100)
# t.goto(50, 50)
# turtle.done()

