'''
线程
任何进程默认会启动一个线程，
这个线程称为，主线程，主线程可以启动新的子线程
'''

import threading

if __name__ == '__main__':

    # current_thread() 当前线程的实例
    # .name()  当前线程的名字
    print('主线程%s启动'%(threading.current_thread().name))