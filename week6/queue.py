class Node:

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue is empty!")
        value_ = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value_

    def empty(self):
        return self.head is None

    def pprint(self):
        vals = []
        while self.head is not None:
            vals.append(str(self.head.value))
            self.head = self.head.next
        return "->".join(vals)


queue = Queue()
queue.enqueue(5)
print(queue.pprint())
# print(queue.dequeue())
