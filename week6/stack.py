class Node:

    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link


class Stack:

    def __init__(self):
        self.start = None

    def empty(self):
        return self.start is None

    def push(self, el):
        if self.empty():
            self.start = Node(el)
        else:
            new = Node(el, self.start)
            self.start = new

    def pop(self):
        if self.empty():
            raise "Empty stack!"
        else:
            value = self.start.value
            self.start = self.start.link
            return value

    def pprint(self):
        res = []
        while self.start is not None:
            res.append(str(self.start.value))
            self.start = self.start.link

        return "->".join(res)


def main():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    print(stack.pop())
    print(stack.pprint())


if __name__ == '__main__':
    main()
