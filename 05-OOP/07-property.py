'''
    装饰器
    方法也可以像属性一样调用
    用来给属性增加 getter 和 setter 方法的
'''

class Employee:

    @property
    def salary(self):
        print('salary run ...')
        return 10

e = Employee()
# e.salary() #方法的调用

# 还可以在 salary 前面加上装饰器,然后像属性一样调用
print(e.salary)

# e.salary = 20 # 像属性一样，但是不能赋值