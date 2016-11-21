class Node:

    def __init__(self, value=None, prev=None, nextv=None):
        self.value = value
        self.next = nextv
        self.prev = prev

    def get_next(self):
        if self.next is not None:
            return self.next
        else:
            return None

    def get_prev(self):
        if self.prev is not None:
            return self.prev
        else:
            return None


class DoublyLinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = self.tail = None
        self.length = length

    def append(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.length += 1
        return self.length

    def index(self, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range!")
        temp = self.head
        for idx in range(index):
            temp = temp.next
        return temp

    def size(self):
        return self.length

    def remove(self, index):
        if index < 0 or index > self.length:
            raise IndexError
        ltemp = self.index(index)
        if index == 0:
            self.head = self.head.next
        else:
            self.index(index - 1).next = self.index(index + 1)
            self.index(index + 1).prev = self.index(index - 1)
        self.length -= 1
        return ltemp.value

    def pprint(self):
        temp = self.head
        res = []
        while temp is not None:
            res.append(str(temp.value))
            temp = temp.get_next()
        return "->".join(res)

    def print_reverse(self):
        temp = self.tail
        res = []
        while temp is not None:
            res.append(str(temp.value))
            temp = temp.get_prev()
        return "->".join(res)

    def to_list(self):
        return [int(el) for el in list(self.pprint().split("->"))]

    def add_at_index(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError
        if index == 0:
            self.add_first(data)
        else:
            new_el = Node(data)
            if self.index(index) == self.length:
                self.append(new_el)
            else:
                new_el.prev = self.index(index - 1)
                new_el.next = self.index(index)
                self.index(index).prev = new_el
                self.index(index - 1).next = new_el
            self.length += 1
        return self.index(index)

    def add_first(self, data):
        new_el = Node(data)
        new_el.next = self.head
        new_el.prev = None
        self.head = new_el
        self.length += 1
        return self.head

    def add_list(self, listy):
        if type(listy) != list:
            raise TypeError
        for el in listy:
            self.add_element(el)
        return self.pprint()

    def add_linked_list(self, DLinkedlist):
        while DLinkedlist.head is not None:
            self.add_element(DLinkedlist.head.value)
            DLinkedlist.head = DLinkedlist.head.next
        return self.tail.value

    def ll_from_to(self, start_index, end_index):
        new_list = DoublyLinkedList()
        for idx in range(start_index, end_index + 1):
            new_list.add_element(self.index(idx).value)
        return new_list.pprint()

    def pop(self):
        return self.remove(self.length - 1)

    def reduce_to_unique(self):
        lst = self.to_list()
        unique = []
        for el in lst:
            if el not in unique:
                unique.append(el)
        new_ll = DoublyLinkedList()
        for el in unique:
            new_ll.append(el)
        self = new_ll
        return self.pprint()
