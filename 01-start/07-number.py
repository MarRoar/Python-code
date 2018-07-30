# -- coding: utf-8 --
'''
    运算符
'''
print(1+1) #加法
print(4-1)
print(4*3)
print(4/2) # 浮点数除法 只有在 3.x 版本的才有 2.x 的值还是整数
print(4//2) # 整数除法

print(7%3) # 模取余
print(2**3) # 幂次方 2 的 3次方

# divmod(x,y) 这个函数是同时得到商和余数，返回的是一个元组
print(divmod(13,3))

'''
    int()实现类型转换
    1、浮点数直接舍去小数部分 int(9.9) => 9
    2、布尔类型的转换 True => 1, False => 0
    3、字符串符合整数格式（浮点数格式不行）则直接转换成对应整数，否则报错
'''

print('------------- int() 转换 -----------------')
print(int(9.9))
print(int(True))
print(int(False))

print(int('123'))
# print(int('12.1a')) 这种情况会报错


