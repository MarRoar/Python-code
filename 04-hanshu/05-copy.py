
'''
    浅拷贝和深拷贝
'''

import  copy

def testCopy():
    '''浅拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print('a:', a)
    print('b:', b)

    b.append(30) # 这里面的值不同，就是因为浅拷贝，就是最外层的对象不一样
    b[2].append(7) # 因为地址引用的一样，所以数据的值一样。

    print('浅拷贝后')
    print('a:', a)
    print('b:', b)

# testCopy()
def testDeepCopy():
    '''深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print('a:', a)
    print('b:', b)

    b.append(30) #
    b[2].append(7) #

    print('深拷贝后')
    print('a:', a)
    print('b:', b)

testDeepCopy()