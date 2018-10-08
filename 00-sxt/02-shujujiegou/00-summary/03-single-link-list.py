'''
单向链表

单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在

'''

class Node(object):
    '''单向链表的节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleLinkList(object):
    '''单链表'''

    def __init__(self):
        self.__head = None

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

        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        cur = self.__head
        node = Node(item)

        if cur == None:
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None

        while cur != None:
            if cur.elem == item:
                # 判断是否是第一
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next

        return False

singList = SingleLinkList()

singList.add("a")
singList.add("b")
singList.append("c")
singList.append("d")
singList.append("e")
singList.append("f")
singList.append("g")

print(singList.is_empty())
print(singList.length())
singList.travel()

print("search", singList.search(1))

singList.remove("b")

singList.travel()

singList.insert(3, 3)
singList.travel()