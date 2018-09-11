'''


Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小

'''

class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''往队列中添加一个item 元素'''
        self.items.insert(0, item)

    def dequeue(self):
        '''从队列头部删除一个元素'''
        return self.items.pop()

    def is_empty(self):
        '''判断一个队列是否为空'''
        return len(self.items) == 0

    def size(self):
        '''返回队列的大小'''
        return len(self.items)

