'''
装饰器
'''

def makBlod(fn):
    def wrappen():
        return "<b>" + fn() + "</b>"
    return wrappen

def makItalic(fn):
    def wrappen():
        return "<i>" + fn() + "</i>"
    return wrappen

@makBlod
def test1():
    return "hello world - 01"

@makItalic
def test2():
    return "hello world - 02"

@makBlod
@makItalic
def test3():
    return "hello world - 03"

print(test1())
print(test2())
print(test3())