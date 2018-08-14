'''
    写一个文件读写的程序，并在其中加入异常处理
'''
#
# f = open("test.txt", 'w')
# f.write("hello world")
# f.close()
#
# fr = open("test.txt", 'r')
# result = fr.read()
# print(result)
# fr.close()

try:
    f = open("test.txt", 'w')
    f.write("hello world.....")
except Exception as e:
    print(e.args)
finally:
    f.close()