'''
    自定义异常
    以及抛出自定义异常
'''

class GenderException(Exception):

    def __init__(self):
        super().__init__()
        self.args = '性别只能为男或者女'
        self.errMes = '性别只能为男或者女'

class Student:

    def __init__(self, name, genger):
        self.name = name
        # self.__gender = genger
        self.set_gender(genger)

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        # 这里在设置的时候有可能有不符合要求
        # 我们可以自定义一个异常类
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            # 在这里抛出异常
            raise GenderException()

    def show_info(self):
        print("我是 %s, 我的性别是 %s"%(self.name, self.__gender))

try:
    s = Student('mar', '男1')
except Exception as e:
    print(e.args)
    print(e.errMes)

# s = Student('mar', '男')
# try:
#     s.set_gender(123)
# except Exception as e:
#     print(e.errMes)
#
# s.show_info()

# Exception 是继承的 BaseException
# print(Exception.mro())