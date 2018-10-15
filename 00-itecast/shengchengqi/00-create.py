'''
列表生成式
'''

L = [ x*2 for x in range(5)]
print(L)

G = (x*2 for x in range(5))
print(G)

print(next(G)) #0
print(next(G)) #2
print(next(G)) #4
print(next(G)) #6
print(next(G)) #8