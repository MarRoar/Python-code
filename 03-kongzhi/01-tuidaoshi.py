'''
    推导式的创建
    1、列表推导式
    2、字典推导式
    3、集合推导式
    4、生成器推导式(元组)
'''

# 列表推导式
a = [ x*2 for x in  range(1,50) if x%5 ==0]
print(a)

a = []
for x in range(1, 50):
    if x%5 == 0: a.append(x*2)
print(a)

cells = [(row, col) for row in range(1,5) for col in range(1,5)]
print(cells)

# 字典推导式
my_text = "i love you, i love more, i love night"
my_count = { c: my_text.count(c) for c in  my_text}
print(my_count)

r = {}
for c in my_text:
    r[c] = my_text.count(c)
print(r)

# 集合
c = {c for c in range(1,5)}
print(c)

# 元组
g = (x for x in range(1,6))
print(tuple(g))