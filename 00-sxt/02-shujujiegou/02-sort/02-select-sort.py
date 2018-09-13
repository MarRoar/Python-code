'''
选择排序

选择排序是每次找出最小的索引，
然后替换数据的位置

'''

def select_sort(aList):
    '''选择排序'''
    l = len(aList)

    for j in range(l - 1):
        min_index = j
        for i in range(min_index + 1, l - 1):
            if aList[min_index] > aList[i]:
                min_index = i
        # 循环一遍后找到最小的索引
        aList[j], aList[min_index] = aList[min_index], aList[j]


a = [10, 2, 80, 1, 99]
select_sort(a)
print(a)
# print(l)

