'''
简单聊天功能
'''

from socket import *
import time
from multiprocessing import Process

# udpSocket = socket(AF_INET, SOCK_DGRAM)
# bindAdd = ('', 7788)
# udpSocket.bind(bindAdd)

def sendData():

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAdd = ('', 8080)
    udpSocket.bind(bindAdd)

    while True:
        ac = input("请输入: ")

    # print(a.encode('GB2312'))
    a = "hello"

    udpSocket.sendto(a.encode('GB2312'), ('192.168.24.1', 7788))
    udpSocket.close()

def receiveData():

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAdd = ('', 8089)
    udpSocket.bind(bindAdd)

    while True:
        recvData = udpSocket.recvfrom(2048)
        print('【%s】%s.%s' % (time.ctime(), recvData[1], recvData[0].decode('GB2312')))
    udpSocket.close()

if __name__ == '__main__':

    pReceive = Process(target=receiveData)
    pSend = Process(target=sendData)

    pReceive.start()
    pSend.start()

    pReceive.join()
    pSend.join()

