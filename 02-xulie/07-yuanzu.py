# -- coding:utf-8 --
'''
    元组
        1、元组的元素不能修改
            a = (10,20,30,40,50)
            print(a[0])
            #如果要修改的话就报错
            a[1] = 25
        2、元组排序 sorted(tupleObj) 返回一个列表,之前的元组不会改变
            a = (20, 80, 10, 1, 60)
            b = sorted(a)
            print(b)
        3、zip方法
            a = [10, 11, 12]
            b = [20, 21, 22]
            c = [30, 31, 32]
            d = zip(a, b, c)
            print(list(d))
        4、元组直接相加
            a = (1, 2)
            b = (3, 4)
            c = 1, 2
            d = 3, 4
            print(a + b)
            print(c + d)
'''



