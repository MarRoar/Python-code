
'''
    函数也是对象
'''

def test01():
    print('le')

test01()

# 下面可以说明，这个函数也是对象
# 把地址给 c
c = test01
c()

print(id(test01))
print(id(c))
# 地址是相同的