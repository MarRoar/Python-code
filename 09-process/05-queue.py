'''
进程间的通信
queue
'''
from  multiprocessing import Process
from multiprocessing import Queue

def run1(q):
    q.put("hello")
    q.put("hello")

def run2(q):
    print('before,',q.qsize())
    print(q.get()) # 直到拿到信息才会继续向下执行
    print(q.qsize())

    # block 是否阻塞
    # timeout 超时的时间设置
    # print(q.get(block=True, timeout=1))

if __name__ == '__main__':
    q = Queue(30) #参数是代表 最大信息的个数
    # 多个进程间是共享一个队列对象的
    # q.put("消息1")
    # print(q.full()) # 判断这个队列是否被存满

    p1 = Process(target=run1, args=(q,))
    p2 = Process(target=run2, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
