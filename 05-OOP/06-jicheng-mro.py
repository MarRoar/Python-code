'''
    继承
    mro() 方法 可以查看类的层次结构
'''

class AA:

    def aa(self):
        print('aa')

    def say(self):
        print('say AA')

class BB:

    def bb(self):
        print('bb')

    def say(self):
        print('say BB')

# class CC(BB, AA):
class CC(AA, BB):

    def cc(self):
        print('cc')

c = CC()
print(CC.mro())
# 到底是先调用哪一个 say 呢
c.say()

# 在继承的时候，哪一个在前面，先调用哪一个
# 比如 class CC(AA, BB) 则先调用 AA 的方法

