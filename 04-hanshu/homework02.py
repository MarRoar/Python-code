'''

'''

def compute(n):
    if type(n) != type(1) or n < 0:
        print("请输入大于0的数字")
        return

    sum = 0
    for i in range(1, n + 1):
        sum += i/(i+1)
    return sum

a = compute(2)
print(a)

