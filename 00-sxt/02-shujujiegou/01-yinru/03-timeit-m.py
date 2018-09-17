
import timeit
def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0, i)

timer6 = timeit.Timer("t6()", "from __main__ import t6")
print("append", timer6.timeit(1000))

timer7 = timeit.Timer("t7()", "from __main__ import t7")
print("insert(0)", timer7.timeit(1000))