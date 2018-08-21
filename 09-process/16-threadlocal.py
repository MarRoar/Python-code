'''
 ThreadLocal 变量
 就是这个全局变量是个字典，
 并且是全局变量
 并且在每个线程里面，他是只有他自己的副本
'''

import threading

local_school = threading.local()

def p_student():
    std = local_school.student
    print("Hello %s (in %s)"%(std, threading.current_thread().name))

def p_thread(name):
    local_school.student = name
    p_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=p_thread, args=("张三", ), name="t1")
    t2 = threading.Thread(target=p_thread, args=("李四", ), name="t2")

    t1.start()
    t2.start()