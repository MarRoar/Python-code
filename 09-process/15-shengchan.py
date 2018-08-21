'''
生产者 消费者模式
'''
import threading
from queue import Queue
from time import sleep

class Pro(threading.Thread):
    '''用来生产产品'''
    def run(self):
        global qu
        count = 0
        while True:
            if qu.qsize() < 1000:
                count += 1
                msg = "生成产品" + str(count)
                print(msg)
            sleep(1)
class Con(threading.Thread):
    '''用来消费产品'''
    def run(self):
        global qu
        while True:
            if qu.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + str(qu.get())
                    print(msg)
            sleep(1)

if __name__ == '__main__':
    # 用来存放产品的队列
    qu = Queue()

    # 用来开始生产产品的
    for i in range(500):
        qu.put("初始生产" + str(i))

    # 启动2个线程来生产，
    for i in range(2):
        p = Pro()
        p.start()

    # 启动5线程来消费
    for i in range(5):
        c = Con()
        c.start()