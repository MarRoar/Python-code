'''
简单聊天功能
这是半双工的，就是不能同时接收和发送数据
'''

from socket import *
import time

udpSocket = socket(AF_INET, SOCK_DGRAM)
bindAdd = ('', 7088)
udpSocket.bind(bindAdd)

while True:
    recvData = udpSocket.recvfrom(2048)
    print('【%s】%s.%s'%(time.ctime(), recvData[1], recvData[0].decode('GB2312')))
    a = input("请输入: ")
    udpSocket.sendto(a.encode('GB2312'), ('192.168.24.1', 8080))

udpSocket.close()
