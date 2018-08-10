'''
    异常的传递，
'''

def test1():
    print("-" * 10 + "test1开始" + '-' * 10)
    # 异常
    print(aa)
    '''
        在 test1 这个函数里面出现了异常，就在这里找有没有捕获异常的操作，
        如果没有那就看看是谁调用了 test1,
        然后找到了test2 看看test2 有没有捕获异常的操作，
        如果没有那就看看是谁调用了 test2,
        找到 test3 然后发现 test3 里面有异常的捕获

        如果 test3 里面也没有捕获异常的话，就会把这个问题给Python解释器，就是报错了
    '''
    print("-" * 10 + "test1结束" + '-' * 10)
def test2():
    print("-" * 10 + "test2开始" + '-' * 10)
    test1()
    print("-" * 10 + "test2结束" + '-' * 10)

def test3():
    print("-" * 10 + "test3开始" + '-' * 10)
    # test2()
    try:
        test2()
    except:
        pass
    print("-" * 10 + "test3结束" + '-' * 10)

test3()