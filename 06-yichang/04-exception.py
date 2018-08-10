
'''
    except (Exception, ValueError, ZeroDivisionError) as e:
        使用元组存储异常的时候，多个异常之间是没有顺序要求的
'''



a = input("请输入除数")
b = input("请输入被除数")

try:
    a = int(a)
    b = int(b)
    c = a / b
    print("商为%g"%c)
except (Exception, ValueError, ZeroDivisionError) as e:
    # 写在元组中的时候 是没有顺序的，
    print(type(e))
    # 错误信息
    # 在 BaseException 里面存储的 一个属性 args 这里面存储的是异常的错误信息
    print(e.args)
    print("遇到异常")

