class Node:

    def __init__(self, value=None, prev=None, nexty=None):
        self.value = value
        self.next = nexty
        self.prev = prev


class LinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = self.tail = None
        self.length = length

    def add_element(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.prev = self.tail
            self.tail.next = Node(data)
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
        self.length -= 1
        return ltemp.value

    def pprint(self):
        temp = self.head
        res = []
        while temp is not None:
            res.append(str(temp.value))
            temp = temp.next
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
            self.index(index - 1).next = new_el
            if self.index(index) == self.length:
                self.tail.next = new_el
                new_el = self.tail
            else:
                new_el.next = self.index(index)
            self.length += 1
        return self.index(index).value

    def add_first(self, data):
        new_el = Node(data)
        new_el.next = self.head
        self.head = new_el
        self.length += 1
        return self.head.value

    def add_list(self, listy):
        if type(listy) != list:
            raise TypeError
        for el in listy:
            self.add_element(el)
        return self.pprint()

    def add_linked_list(self, Linkedlist):
        while Linkedlist.head is not None:
            self.add_element(Linkedlist.head.value)
            Linkedlist.head = Linkedlist.head.next
        return self.tail.value

    def ll_from_to(self, start_index, end_index):
        new_list = LinkedList()
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
        new_ll = LinkedList()
        for el in unique:
            new_ll.add_element(el)
        self = new_ll
        return self.pprint()
