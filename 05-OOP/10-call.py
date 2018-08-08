'''
   __call__ 方法

   函数  a() 这样就可以调用
   那么对象 obj() 如果这样写的话其实是调用 __call__ 方法
'''

a = 1
b = 2
c = a + b
# 这个加号后面进行的解释为
d = a.__add__(b)

class salaryAccount:

    def __call__(self, *args, **kwargs):
        # 这个参数是可以修改的。
        print("算工资了...")
        return 100

s = salaryAccount()

a = s()
print(a)