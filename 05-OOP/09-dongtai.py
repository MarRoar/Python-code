'''
    方法的动态性

    1> 添加新方法
    2> 修改老方法

    一切都是对象,所以就可以修改了
'''

class Person:

    def work(self):
        print('努力上班')

def play_game(s):
    print('{0}在玩游戏'.format(s))

def work2(s):
    print('努力上班，挣钱养家')

Person.play = play_game

p = Person()
p.work()
p.play()  # 函数调用的本质 p.play() => Person.play

Person.work = work2

p.work()
