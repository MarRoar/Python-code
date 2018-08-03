''''
    递归调用的内存分析s
'''

def t1(n):
    print('现在是n = ', n)

    if n == 0:
        print('over')
    else:
        t1(n - 1)

    print('t1****', n)

t1(5)