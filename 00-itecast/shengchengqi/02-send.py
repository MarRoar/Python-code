''''''

def test():
    i = 0
    while i < 5:
        t = yield i
        print(t)
        i += 1

a = test()
# 如果在生成器里面第一次使用 send 的话就会报错啦！
a.send(None)