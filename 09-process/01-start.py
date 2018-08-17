'''
进程
'''
from multiprocessing import Process
from time import sleep

def run(name):
    print("子进程运行中%s"%(name))
    sleep(2)

# 在 window 子进程会 import 他的启动文件
print(__name__)
if __name__ == '__main__':
    print("父进程启动")
    # p = Process(target=run, args=('test',))
    p = Process(target=run, args=('test',), name="pro1")

    print("子进程要启动")
    p.start()
    print(p.name) # 每个进程 系统分配的名字 这个名字也可以修改
    print(p.pid) # 进程实例ID

    p.join() # 主要进程等待子进程执行完
    print("子进程结束")