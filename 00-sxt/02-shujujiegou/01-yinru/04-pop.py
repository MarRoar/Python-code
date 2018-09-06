'''

数据出入在 list 开始位置和结束位置所用的效率差别还是挺大

'''

from timeit import Timer

def f1():
    x = []
    for i in range(20000):
        x.append(i)

def f2():
    x = []
    for i in range(20000):
        x.insert(0, i)


t1 = Timer("f1()", "from __main__ import f1")
print("x.pop(0)", t1.timeit(number=1000))


t2 = Timer("f2()", "from __main__ import f2")
print("x.pop(0)", t2.timeit(number=1000))

