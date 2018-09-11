'''
单循环链表
'''
class Node(object):
    '''单向链表的节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None

class SingleCircleLinkList(object):
    '''单循环链表'''

    def __init__(self, node = None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        if cur == None:
            return
        else:
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            print(cur.elem)

    def add(self, item):
        '''链表头部添加元素'''
        cur = self.__head
        node = Node(item)
        if cur == None:
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            self.__head = node
            cur.next = node

    def append(self, item):
        '''链表尾部添加元素'''
        cur = self.__head
        node = Node(item)
        if cur == None:
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cur = self.__head
            pre = None
            node = Node(item)
            while count < pos:
                count += 1
                pre = cur
                cur = cur.next
            node.next = cur
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        '''
            注意
            1、为空
            2、第一个节点的情况
                a) 列表只有一个节点
                b) 列表有多个节点
            3、在中间的情况
        '''
        if self.is_empty():
            return None

        cur = self.__head
        pre = None

        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next

                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # 链表的最后一个元素
        if cur.elem == item:
            if pre == None:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        if cur == None:
            return False

        while cur.next != self.__head:
            if cur.elem == item:
                return True
            cur = cur.next

        if cur.elem == item:
            return True
        return False

n = Node("1")
sc = SingleCircleLinkList()

sc.add("a")
sc.add("b")
sc.add("c")
sc.add("d")
sc.add("e")
sc.add("f")
sc.append("11")
sc.insert(2, '22')

sc.travel()

sc.remove('f')
sc.travel()

