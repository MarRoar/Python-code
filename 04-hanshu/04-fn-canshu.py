
'''
    参数传递的时候 是地址传递
    可变对象和不可变对象

'''

# 可变对象
b = [10, 20]
def f1(m):
    m.append(30)
f1(b)
print(b)
# 从打印的结果可以看出，m 和 b 引用的是同一个对象

print('不可变对象')
# 不可变对象
a = 10
def f2(n):
    print(id(n))
    n = n + 1
    print('操作之后的id= {0}'.format(id(n)))

print(id(a))
f2(a)
print(a)
