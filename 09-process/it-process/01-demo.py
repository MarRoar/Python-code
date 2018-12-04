'''
进程
'''
'''
进程池
'''

import threading
import time

g_num = 0

def w1():
    print("子线程%s"%(threading.current_thread().name))
    global g_num
    for i in range(10000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
    print("nu---", g_num)

def w2():
    print("子线程%s"%(threading.current_thread().name))
    global g_num
    # print(mutex.acquire(True))
    # print('----')
    for i in range(10000):
        mutexFlag = mutex.acquire(True)

        if mutexFlag:
            g_num += 1
            mutex.release()

    print("nu---==", g_num)


if __name__ == '__main__':
    print("主线程%s"%(threading.current_thread().name))

    mutex = threading.Lock()

    t = threading.Thread(target=w1)
    t.start()

    t2 = threading.Thread(target=w2)
    t2.start()
