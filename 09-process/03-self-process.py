'''
自定义类进程
'''
import multiprocessing
import time

class ClockProcess(multiprocessing.Process):

    def run(self):
        ''' 这里就是要重写的方法 '''
        n = 5
        while n > 0:
            print(n)
            time.sleep(1)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess()
    p.start()
    p.join()
    print("主线程执行结束...")