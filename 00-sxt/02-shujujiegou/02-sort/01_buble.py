'''
冒泡排序
'''

def bubble_sort(aList):
    n = len(aList)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
