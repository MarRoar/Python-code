
from multiprocessing import Process

def run():
    print("run1")

if __name__ == '__main__':
    p = Process(target=run)

    p.start()

    p.join()