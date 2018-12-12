# coding:utf-8

class Stack(object):
    """栈"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        # 返回栈顶元素
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        pass

    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)


class Dqueue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.__list.pop(0)
        else:
            return None

    def remove_rear(self):
        if not self.is_empty():
            return self.__list.pop(-1)
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Dqueue()
    s.add_front(1)
    s.add_front(2)
    s.add_front(3)
    s.add_front(4)
    s.add_front(5)
    s.add_front(6)
    print(s.remove_front())
    print(s.remove_rear())
