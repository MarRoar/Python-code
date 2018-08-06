'''
    Python 没有方法重载
        方法签名 (方法名, 参数个数，参数类型)
    Python 中，方法的参数没有类型,所以就没有必要重载了
'''

class A:

    def say(self):
        print('hello 01')

    def say(self, name):
        print('hello 02', name)

# A().say() 报错，只有最后一个是有效的
A().say('sd')


