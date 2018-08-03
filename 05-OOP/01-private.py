
'''
    私有属性和私有方法

    怎么在外部访问私有属性
'''

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.__age = age # 加连个下划线属性变成私有的

    def __work(self):
        print('私有方法', self.__age)

e = Employee('mar', 12)
print(e.name)

# print(e.age) # 私有属性不能直接访问

'''
    通过  实例对象._类名__属性名
    这种方式来访问私有属性
'''
print(e._Employee__age)
print(dir(e))

#私有方法调用
e._Employee__work()

print(dir(Employee))
Employee._Employee__work(e)