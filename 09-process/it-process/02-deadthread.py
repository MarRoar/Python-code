import threading
import time

class AThread(threading.Thread):

    def run(self):
        if mutexA.acquire():
            print("dododo AAAAAAA")
            time.sleep(1)
            if mutexB.acquire():
                print("dododo BBBBB")
                mutexB.release()

            mutexA.release()

class BThread(threading.Thread):

    def run(self):
        if mutexB.acquire():
            print("wwww AAAAA")
            time.sleep(1)
            if mutexA.acquire():
                print("wwwwwww BBB")
                mutexA.release()

            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':

    a = AThread()
    a.start()

    b = BThread()
    b.start()