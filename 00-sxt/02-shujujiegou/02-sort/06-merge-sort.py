'''
归并排序

1、首先是分组，将所要排序的列表先一分为二，递归这去拆分
2、然后将两个列表第一个元素进行比较，将小的数据push到新的列表里面。

比如： [90, 63, 20]
1、先一分为二 left_li = [90], right_li = [63]
2、然后从左右两边各取第一个数据进行比较
    left_li[0] >= right_li[0]
    将小的数据push到 result[] 里面,
上面这些是最基本的原理


'''

def merge_sort(aList):

    n = len(aList)

    if n <= 1:
        return aList
    mid = n//2

    left_li = merge_sort(aList[:mid])
    right_li = merge_sort(aList[mid:])

    left_pointer, right_pointer = 0, 0
    result = []
    print('拆分 - left = ', left_li)
    print('拆分 - right = ', right_li)

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        # print(left_li[left_pointer], right_li[right_pointer])

        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    print('result = ', result)

    return result

if __name__ == "__main__":

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # li = [54, 26, 93]
    # print(li)
    a = merge_sort(li)
    # print(li)
    # print(a)
