'''
输入三角形三个顶点的坐标，若有效则计算三角形的面积；如坐标无效，则给出提
示
'''

'''
    1、判断这三个点能否组成三角形
    2、求面积
'''
import  math
def calculateArea(x1, y1, x2, y2, x3, y3):

    def calLine(x1, y1, x2, y2):
        '''计算两个点之间的距离'''
        l = (x2 - x1) ** 2 + (y2 - y1) ** 2
        return math.sqrt(l)
    # 1、计算三个点两两之间的距离,然后判断是否可以组成三角形
    lines = [calLine(x1, y1, x2, y2), calLine(x2, y2, x3, y3) , calLine(x1, y1, x3, y3)]
    lines.sort()
    if lines[0] + lines[1] < lines[2]:
        print('输入的坐标无效')
        return None

    # 2、输入面积
    return (x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)/2

a = calculateArea(x1 =0, y1 = 0, x2 = 3, y2 = 0, x3 = 0, y3 = 3)
print(a)
