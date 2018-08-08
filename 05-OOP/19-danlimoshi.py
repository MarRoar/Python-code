# 设计模式 - 单例模式
# 单例模式，就是 对象只实例化一次

class MySingleton:

    __obj = None
    __init_flag = True

    '''
    1、创建一个类对象用来存放实例对象
    2、重写 __new__ 方法，在里面判断这个对象是否为 None
    3、如果为空的话就是创建，如果不为空就返回之前创建的

    4、但是只有一个变量的时候发现 init 了多次,所以再加一个变量来计算 init 的次数
    '''

    def __new__(cls, *args, **kwargs):

        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    # 但是初始化 init 了 两次
    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init...")
            self.name = name
            MySingleton.__init_flag = False

a = MySingleton('a')
b = MySingleton('b')
print(a)
print(b)