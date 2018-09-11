'''
双端队列

Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小

'''

class Deque(object):

    def __init__(self):
        self.items = []

    def add_front(self, item):
        '''从队头加入一个item元素'''
        self.items.insert(0, item)

    def add_rear(self, item):
        '''从队尾加入一个item元素'''
        self.items.append(item)

    def pop_front(self):
        '''从队头删除一个item元素'''
        return self.items.pop(0)

    def pop_rear(self):
        '''从队尾删除一个item元素'''
        return self.items.pop()

    def is_empty(self):
        '''判断双端队列是否为空'''
        return len(self.items) == 0

    def size(self):
        '''返回队列的大小'''
        return len(self.items)