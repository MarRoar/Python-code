''''
    文件操作
    打开文件
    关闭文件
'''

# 写文件
'''
f = open('01-text.txt', 'w')
f.write("hello wolrd")
f.close()
'''

# 读文件
'''
    f.read(num) num 表示读取几个字符，如果不传的话，读取整个文件
    f.readlines()  一行一行的读取文件放在列表里面，一般不用
    f.readline()  读取一行
'''

f = open("01-text.txt", 'r')
content = f.read()
print(content)
f.close()