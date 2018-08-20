'''
进程池间的通信
'''

from multiprocessing import Manager,Process,Pool
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
    q = Manager().Queue()

    po = Pool(3)
    po.apply_async(write, (q,))
    po.apply_async(read, (q,))

    po.close()
    po.join()
    print("读取结束")
