'''
UDP socket 发送
'''

from socket import *
s = socket(AF_INET, SOCK_DGRAM)

add = ('192.168.24.1', 8080)
ss = 'ninini'
s.sendto(ss.encode('utf-8'), add)
s.close()