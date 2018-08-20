'''
线程
任何进程默认会启动一个线程，
这个线程称为，主线程，主线程可以启动新的子线程
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

# 不要 start() 多次
# t = threading.Thread(target=saySorry)
# t.start()
#
# t.start()

