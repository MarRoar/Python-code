'''
深拷贝和浅拷贝的问题

1、Python有个copy 模块，里面有
    copy.copy() 浅拷贝
    copy.deepcopy() 深拷贝
2、
'''

import copy

a = [11, 22, 33]
b = [44, 55, 66]

c = (a, b)
d = [a, b]
print("---------不可变------------------")
print('c', id(c))
e = copy.copy(c)
print('e', id(e))
print('---------可变--------------------')

print('d', id(d))
f = copy.copy(d)
print('f', id(f))
