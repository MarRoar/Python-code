'''

快速排序

'''

def quick_sort(aList, first, last):

    if first >= last:
        return

    min_val = aList[first]
    low_index = first
    hight_index = last

    while low_index < hight_index:
        # height 左移动
        while low_index < hight_index and min_val <= aList[hight_index]:
            hight_index -= 1
        aList[low_index] = aList[hight_index]

        # low 右移动
        while low_index < hight_index and min_val > aList[low_index]:
            low_index += 1
        aList[hight_index] = aList[low_index]

    aList[low_index] = min_val

    # 左边
    quick_sort(aList, first, low_index - 1)
    # 右边
    quick_sort(aList, low_index + 1, last)


if __name__ == "__main__":

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)