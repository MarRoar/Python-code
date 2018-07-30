# -- coding: utf-8 ---
'''
1> 字符串编码
    ord(str) 将str 转换成unicode编码
    chr(num) 将十进制数字转换成字符串

    len(str) 查看字符的个数
2> 字符串拼接
    1、用 + 号 'hello' + 'world'
    2、将多个字符串放在一起实现拼接
        'hello'' world' => 'hello world
3> 字符串复制
    str * n 将字符串 * n 个就可以
4> 不换行打印
    print() 其实也就是 print() 打印函数的参数问题
    print('hello') # 打印一个 hello ，这种情况也就是 print('hello', end='\b')
    end = '表示以什么结尾'
    print('hello', end='&&')
5> str()
    str()函数将其他类型，转换成 字符类型
    str(True) => 'True'
    str(123) => '123'
6> str[index] 读取字符
    1、正向读 0 <= index <= len(str) - 1
    2、反向读 -len(str) <= index <= -1
        s = 'hello'
        print(len(s))
        print(s[0])
        print(s[len(s) - 1])  #len(str) - 1

        print(s[-1])
        print(s[-len(s)])
7> replace() 字符替换
    Python 是不能 str[n] = '换' 替换的
    a = 'abcdefg'
    b = a.replace('c', '哈')
    print(b)
8> slice 字符串切片操作
    Python中 用 [] 来截取字符串
    [start开始偏移量: end终止偏移量: step步长]
    start 默认的是开始的位置 0
    end 默认的是结束的位置 len(s)
    step 默认的是 1

    这三个数为负数的情况
    s = 'abcdefghijk'
    s[-3:] => 'ijk'  最后三个字符
    s[-8:-3] 倒数第8个和倒数第3个
    s[::-1] 步长为负数，从右到左 (也就是字符反转)
9> split() 将字符串分割,
    s = 'to be or not to be'
    s.split()
    s.split('be')
10> join()将字符串连接起来
    a = ['a', 'b']
    '*'.join(a)
    'a*b'
11> 字符串驻留机制
    Python支持字符串驻留机制，对于符合标识符规则的字符串（仅包含字符下划线数字）会启动字符串驻留机制。
    a = 'ad_13'
    b = 'ad_13'
    a is b
    True
12> in 操作, 字符是否在字符串中
    'a' in 'marui' => True
13> 字符串查找
    str.startswith('a') #是否以字符串 'a' 开头
    str.endswith('a')   是否已字符串 'a' 结尾
    str.find('马')   第一次出现字符串 '马' 的位置
    str.rfind('马') 最后一次出现字符 '马' 的位置
    str.count('吗') 字符串中出现 '吗' 的次数
    str.isalnum() 所有的字符是否全部是字符或者数字
14> strip() 去除首位信息
    str.strip() 去除首位的空格
    str.strip('#') 去除首位的 '#' 字符
    str.lstrip() 去除左边的
    str.rstrip() 去除右边的
15> 大小写转换
    str.capitalize() 产生新的字符串 字符串首字母大写
    str.title()  产生新的字符串 每个单词的首字符大写
    str.upper()  产生新的字符串 所有字母转换成大写
    str.lower()  产生新的字符串 所有字母转换成小写
    str.swapcase() 产生新的字符串 所有字母大小写转换
16> 格式排版
    center(num, chart)
    ljust(num, chart)
    rjust(num, chart)

        a = 'Marui'
        # a.center(10, '##') 这种情况会报错
        print(a.center(10,'#'))
        print(a.ljust(10, '#'))
        print(a.rjust(10, '#'))
17> 其他方法
    str.isalnum() 是否为字母或者数字
    str.isalpha() 是否由字母组成(包含汉字)
    str.isdigit() 是否由数字组成
    str.isspace() 是否为空白符
    str.isupper() 是否为大写字母
    str.islower() 是否为小写字母
18> format() 字符串格式化

'''



