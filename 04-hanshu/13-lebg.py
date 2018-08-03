'''
Python 变量查找规则
'''

# str()
# str = 'global'
def outer():
    # str = 'outer'
    def inner():
        # str = 'inner'
        print(str)
    inner()

outer()