'''
UDP 接收
'''
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
addbind = ('', 50204)
s.bind(addbind)
add = ('192.168.24.1', 8080)

ss = 'nihaoasdfas'
s.sendto(ss.encode(), add)
rec = s.recvfrom(2048) # 接收消息，参数是数据的最大值

print(rec)
s.close()