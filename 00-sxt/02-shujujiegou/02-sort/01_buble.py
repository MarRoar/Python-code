'''
冒泡排序
'''

def bubble_sort(aList):
    n = len(aList)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


a = [3, 1, 9, 0,2, 4]

bubble_sort(a)

print(a)

# 课件的方法
print(list(range(len(a) - 1, 0, -1)))
