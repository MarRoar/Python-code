'''
线程共享全局变量

10000000 的 bug
出现这个bug 的问题是
主线程执行完了，但是两个子线程还没有执行完

'''

import threading
import time

num = 0
def work1():
    global num

    for i in range(10000000):
        num += 1

    print("in work1 , number is %d"%num)

def work2():
    global num

    for i in range(10000000):
        num += 1

    print("in work1 , number is %d"%num)


if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.start()

    t2 = threading.Thread(target=work2)
    t2.start()
    print(num)
