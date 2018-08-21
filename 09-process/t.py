"""
    线程，
    任何一个程序都会默认的启动一个进程，和进程里面的一个线程

"""

import threading
import time

def say():
    print("当前线程的名字 {0}".format(threading.current_thread().name))
    time.sleep(1)
    print("I am wrong")

if __name__ == '__main__':
    print("当前线程的名字 {0}".format(threading.current_thread().name))

    for i in range(5):
        t = threading.Thread(target=say)
        t.start()

    print("over")