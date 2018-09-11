'''
双向链表
'''

class Node(object):
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None

class DoubleLinkList(object):
    '''双向链表'''

    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)

        if self.__head == None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        cur = self.__head

        if cur == None:
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            node.prev.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    '''删除第一个元素'''
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                return
            else:
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False

dl = DoubleLinkList()

print("is_empty = ", dl.is_empty())
print("length  = ", dl.length())
dl.add("aa")
dl.add("bb")
dl.add("cc")
dl.append("dd")
dl.append("ee")

dl.travel()

# dl.remove("cc")
dl.remove("bb")
dl.remove('ee')
dl.travel()

# print(dl.search("1"))

dl.insert(0, "00")
dl.insert(2, '22')

dl.travel()