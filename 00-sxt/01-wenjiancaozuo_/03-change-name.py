# 该名字 把 01-text.txt 修改成 03-text.txt

import os

# 修改文件名字
# os.rename('./01-text.txt', '03-text.txt')

# 当前文件的绝对路径
print(os.path.abspath('03-text.txt'))
#F:\MyData\MarLearn\Python\Python-code\00-sxt\01-wenjiancaozuo_\03-text.txt

# 获得文件大小
print(os.path.getsize('03-text.txt'))

# 获取文件列表
l = os.listdir('../01-wenjiancaozuo_')
print(l)