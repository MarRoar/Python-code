'''
线程 锁的用法

mutex = threading.Lock() 创建一个锁对象

mutex.acquire() 加锁

mutex.release() 释放锁

'''

import threading

num = 0

def test01():
    global num
    if mutex.acquire():
        for i in range(1000000):
            num += 1
    print(num)

    mutex.release()

def test02():
    global num
    if mutex.acquire():
        for i in range(1000000):
            num += 1
    print(num)

    mutex.release()

mutex = threading.Lock()

p1 = threading.Thread(target=test01)
p2 = threading.Thread(target=test02)

p1.start()
p2.start()
