'''
希尔排序

希尔排序具体的思路步骤


'''

def shell_sort(aList):
    n = len(aList)
    gap = n // 2

    while gap > 0:

        for j in range(gap, n):

            i = j
            while i > 0:
                if aList[i] < aList[i - gap]:
                    aList[i - gap], aList[i] = aList[i], aList[i - gap]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == "__main__":

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)