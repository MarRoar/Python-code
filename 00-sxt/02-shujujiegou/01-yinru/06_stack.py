'''
栈的操作
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''

class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        '''判断栈是否为空'''
        return len(self.items) == 0

    def push(self, item):
        '''添加一个元素到栈顶'''
        self.items.append(item)

    def pop(self):
        '''弹出元素'''
        return self.items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.items[len(self.items) - 1]

    def size(self):
        '''返回栈的大小'''
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    print(s.is_empty())
    print(s.pop())


