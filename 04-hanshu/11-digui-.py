'''
斐波那契函数
'''

def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)

a = factorial(5)
print(a)