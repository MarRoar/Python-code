'''

'''

import timeit

def t1():
    l = []
    for i in range(1000):
        l = l + [i]
def t2():
    l = []
    for i in range(10000):
        l.append(i)

def t3():
    l = [i for i in range(10000)]

def t4():
    l = list(range(10000))


timer01 = timeit.Timer("t1()", "from __main__ import t1")
print("+", timer01.timeit(number=1000), ' seconds')

timer02 = timeit.Timer("t2()", "from __main__ import t2")
print("append", timer02.timeit(number=1000), ' seconds')

timer03 = timeit.Timer("t3()", "from __main__ import t3")
print("comprehension", timer03.timeit(number=1000), ' seconds')

timer04 = timeit.Timer("t4()", "from __main__ import t4")
print("list range", timer04.timeit(number=1000), ' seconds')

