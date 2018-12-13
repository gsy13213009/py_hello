# coding:utf-8

class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        pass

    def append(self, item):
        """尾部添加"""
        node = Node(item)
        cur = self.__head
        if cur is None:
            self.__head = node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def insert(self, item, index):
        """指定位置添加"""
        node = Node(item)
        if index < 0 or index > self.length():
            return
        cur = self.__head
        for i in range(index - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = cur
        while cur is not None:
            if cur.elem == item:
                if cur is self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False


item = SingleLinkList()
print(item.is_empty())
item.append(1)
item.append(2)
item.append(2)
item.append(2)
item.append(2)
item.append(2)
item.append(2)
item.append(2)
item.append(3)
item.append(4)
item.append(5)
item.add(4)

item.travel()

item.remove(2)

item.travel()

print(item.search(100))
