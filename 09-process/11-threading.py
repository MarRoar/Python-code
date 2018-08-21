'''
线程 用类来实现
'''

import threading

class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print(self)
if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()

    t1.start()
    t2.start()