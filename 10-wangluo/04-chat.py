'''
简单聊天功能
'''

from socket import *
import time
import threading

udpSocket = socket(AF_INET, SOCK_DGRAM)
bindAdd = ('', 7088)
udpSocket.bind(bindAdd)

def sendData():

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAdd = ('', 7088)
    udpSocket.bind(bindAdd)

    while True:
        a = input("请输入: ")
        udpSocket.sendto(a.encode('GB2312'), ('192.168.24.1', 8080))
    udpSocket.close()

def receiveData():

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAdd = ('', 7088)
    udpSocket.bind(bindAdd)

    while True:
        recvData = udpSocket.recvfrom(2048)
        print('【%s】%s.%s' % (time.ctime(), recvData[1], recvData[0].decode('GB2312')))
    udpSocket.close()

if __name__ == '__main__':
    tReceive = threading.Thread(target=receiveData)
    tSend = threading.Thread(target=sendData)

    tReceive.start()
    tSend.start()









udpSocket.close()
