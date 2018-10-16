'''
斐波那契函数，用生成器来
'''

def createNum():
    # print("----satart---")
    a,b = 0, 1
    for x in range(6):
        # print(b)
        # print("befor yiel======")
        yield b
        # print("after yiel")
        a, b = b, a + b
    # print("----end---")
a = createNum()
# print("1")
print(next(a))
# print("2")
print(next(a))
print(next(a))
print(next(a))
