'''
tftp
'''

import struct
from socket import *

cmb_buf = struct.pack("!H9sb5sb", 1, b"test.jpg", 0, b"octet", 0)
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(cmb_buf, ("192.168.1.1", 69))

udpSocket.close()