'''
线程同步

让线程有顺序的执行


'''
import threading

def test01():
    while True:
        if lock01.acquire():
            print("task01---")
        lock02.release()
        break
def test02():
    while True:
        if lock02.acquire():
            print("task02---")
        lock03.release()
        break
def test03():
    while True:
        if lock03.acquire():
            print("task03--")
        lock01.release()
        break

if __name__ == '__main__':

    lock01 = threading.Lock()
    lock02 = threading.Lock()
    lock03 = threading.Lock()

    p1 = threading.Thread(target=test01)

    lock02.acquire()
    p2 = threading.Thread(target=test02)

    lock03.acquire()
    p3 = threading.Thread(target=test03)

    p1.start()
    p2.start()
    p3.start()