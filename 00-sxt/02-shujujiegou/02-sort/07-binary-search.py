'''
二分法查找
'''

def binary_search(aList, item):
    '''递归的方式'''
    n = len(aList)

    if n < 1:
        return False

    mid = n // 2
    first_index = 0
    print(aList[mid], item)

    if aList[mid] == item:
        return True
    elif aList[mid] > item:
        return binary_search(aList[:mid], item)
    else:
        return binary_search(aList[mid + 1:], item)

    return False

def binary_search_01(aList, item):
    '''递归的方式'''
    n = len(aList)
    if n > 0:
        mid = n // 2
        first_index = 0
        print(aList[mid], item)

        if aList[mid] == item:
            return True
        elif aList[mid] > item:
            return binary_search(aList[:mid], item)
        else:
            return binary_search(aList[mid + 1:], item)

        return False

def binary_search_02(aList, item):
    n = len(aList)
    first_index = 0
    last_index = n - 1

    while first_index <= last_index:
        print(first_index, last_index)
        # 取中间值必须在循环里面，不然就不会跳出这个循环了。
        mid = (last_index + first_index) // 2

        if aList[mid] == item:
            return True
        elif aList[mid] > item:
            last_index = mid - 1
        else:
            first_index = mid + 1
    return False


if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # print(binary_search(li, 1))
    # print(binary_search_01(li, 17))

    print(binary_search_02(li, 1))

