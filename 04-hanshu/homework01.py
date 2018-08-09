'''
    作业

    定义一个函数实现反响输出一个整数。比如：输入 3245，输出 5432
'''

def fnReverse(enter):
    '''输入的数据方向输入,比如：输入 3245，输出 5432'''

    '''
        1、首先判断数据类型,如果是 int 的转换成 string
        2、其它数据类型，直接反向输出
    '''
    if type(enter) == type(1):
        enter = str(enter)
    return enter[::-1]

a = fnReverse(123)
b = fnReverse('abcdefg')
print(a)
print(b)

