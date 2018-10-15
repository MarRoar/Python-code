'''
装饰器
'''

def makBlod(fn):
    print("makBlod")
    def wrappen():
        return "<b>" + fn() + "</b>"
    return wrappen

def makItalic(fn):
    print("makItalic")
    def wrappen():
        return "<i>" + fn() + "</i>"
    return wrappen

@makBlod
@makItalic
def test3():
    return "hello world - 03"

print(test3())