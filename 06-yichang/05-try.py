'''
    语法
    try:
    except 异常 as 变量:
    else:
        没有异常执行的代码
    finally:
        最终一定要执行的代码


    案例：将一些字符串数据写入文件中
'''
'''
f = open("05-text.txt", 'w', encoding="utf-8")
f.write("hello")
# write 只能写入 字符串类型的数据
f.write([1, 2, 3])
# 这句话出现了问题，所以下面的代码都没有执行

print("写入完毕")
f.close()
print("关闭文件，谢谢")
'''

try:
    f = open("05-text.txt", 'w', encoding="utf-8")
    f.write("hello")
    f.write([1, 2, 3])
    print("写入完毕")

except Exception as e:
    print(e.args)
else:
    # 没有异常走这里
    print("没有异常")
finally:
    # 无论是否有异常，都会走 finally
    # 最后一定要确保执行的代码
    f.close()
    print("关闭文件，谢谢使用")

