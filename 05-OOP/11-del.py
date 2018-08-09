# __del__ 析构函数

class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))

p1 = Person()
p2 = Person()

del  p2

print("程序结束")
# 程序结束后，p1 也被销毁了