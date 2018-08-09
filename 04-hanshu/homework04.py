#输入一个毫秒数，将该数字换算成小时数，分钟数、秒数


def transformHMS(n):
    s = n/1000
    m = s/60
    h = m/60
    return (h, m, s)

a = transformHMS(5000000)
print(a)