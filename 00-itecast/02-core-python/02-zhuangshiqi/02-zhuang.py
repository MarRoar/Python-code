'''
装饰器
'''

def makeBlod(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makeBlod
def f1():
    return 'hello wolrd - 1'

@makeItalic
def f2():
    return 'hello wolrd - 2'

@makeBlod
@makeItalic
def f3():
    return 'hello wolrd - 3'


print(f1())
print(f2())
print(f3())