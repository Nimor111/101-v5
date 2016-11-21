import unittest
from doubly_linked_list import DoublyLinkedList


class TestDLL(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_get_next(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.index(1).get_next().value, 2)

    def test_get_prev(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.index(2).get_prev().value, 1)

    def test_print_reverse(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.print_reverse(), "3->2->1->5")

    def test_print(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.pprint(), "5->1->2->3")

    def test_add_at_index(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.add_at_index(2, 4).get_prev().value, 1)

    def test_reduce_to_unique(self):
        self.dll.append(5)
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(2)
        self.assertEqual(self.dll.reduce_to_unique(), "5->1->2")


if __name__ == '__main__':
    unittest.main()
