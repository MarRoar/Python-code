'''
进程池
'''
from multiprocessing import Pool
import random, time

def work(num):
    print(random.random()*num)
    time.sleep(2)

if __name__ == '__main__':
    p = Pool(3) # 参数是最大进程数量，默认的话是内核数量
    for i in range(10):
        p.apply_async(work, (i,))

    p.close() # 进程池关闭之后，不再接收新的请求
    p.join() # 等待所有子进程结束，必须放在 close() 之后