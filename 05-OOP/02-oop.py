'''
创建类
    首字母大写，驼峰命名

self 的名字是可以修改的
'''

class Studen:

    def __init__(self, name, score):  # self 当前对象本身,必须在第一个位置, 
        self.name = name
        self.score = score

    def say_score(self): # self 必须是第一个参数
        print('{0}的分数是{1}'.format(self.name, self.score))

s1 = Studen('mar', 99) # 通过类名() 来调用构造函数,没有返回的
s1.say_score()

