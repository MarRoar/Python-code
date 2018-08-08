# 特殊属性

class AA:
    pass

class BB:
    pass

# class CC(BB, AA):
class CC(AA, BB):

    def __init__(self):
        self.nn = 'dict'

    def cc(self):
        print('cc')

c = CC()

print(dir(c)) # 得到类的所有属性
print(c.__dict__)
print(c.__class__) # c 是哪个类
print(CC.__bases__) # CC 的元组
print(CC.mro()) # 类的层次结构

print(AA.__subclasses__())  # 子类列表




