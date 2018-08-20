'''
进程间的通信
queue
'''
from  multiprocessing import Process
from multiprocessing import Queue
import time

def write(q):
    for v in ['a', 'b', 'c']:
        print("开始写入", v)
        q.put(v)
        time.sleep(1)

def read(q):
    while True:
        if not q.empty():
            print("读取到的数据是", q.get())
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    q = Queue(30) #参数是代表 最大信息的个数
    # 多个进程间是共享一个队列对象的
    # q.put("消息1")
    # print(q.full()) # 判断这个队列是否被存满

    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
    print("接收完毕")
