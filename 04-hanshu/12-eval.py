'''
    eval()
'''

eval('print("hello world")')
eval('print("12+12")')
print(eval('12+11'))

a = 10
b = 20
c = eval('a + b')
print(c)

d1 =dict(a = 100, b = 200)
e = eval('a + b', d1) # 改变个eval 的执行上下文
print(e)