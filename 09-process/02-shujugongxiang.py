'''
全局变量在多个进程中不共享，
进程之间的数据是独立的，默认情况下是互不影响
'''
from multiprocessing import Process

num = 1

def run1():
    global num
    num += 5
    print(num)
    print("子进程1运行中,num = {0}".format(num))

def run2():
    global num
    num += 10
    print(num)
    print("子进程1=2运行中,num = {0}".format(num))

if __name__ == '__main__':
    # num = 2
    p1 = Process(target=run1)
    p2 = Process(target=run2)

    p1.start()
    p2.start()
    p1.join()
    # print("nnnn = {0}".format(num))
    p2.join()
    print("子进程结束...............")
    print(num)