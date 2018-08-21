'''
线程

threading.enumerate()
返回当前所有线程的 列表

'''

import threading
import time

def saySorry():
    print("子线程%s启动"%(threading.current_thread().name))
    time.sleep(1)
    print("错哦")

if __name__ == '__main__':

    print('主线程%s启动'%(threading.current_thread().name))

    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()

    print(threading.enumerate())

    while True:
        l = len(threading.enumerate())
        print("当前线程数量 ", l)
        if l <= 1:
            break
        time.sleep(1)

        

# 不要 start() 多次
# t = threading.Thread(target=saySorry)
# t.start()
#
# t.start()

