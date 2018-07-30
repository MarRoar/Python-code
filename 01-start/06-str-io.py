# -- coding: utf-8 --
# 可变字符
import  io
s = "hello world"
#python2.x 需要改动如下 StringIO(unicode(“your string”))
sio = io.StringIO(s)
print(sio.getvalue())

sio.seek(4)
sio.write('p')
print(sio.getvalue())
