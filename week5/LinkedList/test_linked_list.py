import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_pprint(self):
        self.ll.add_element(4)
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.pprint(), "4->5->6->7")

    def test_to_list(self):
        self.ll.add_element(4)
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.to_list(), [4, 5, 6, 7])

    def test_add_at_index(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.add_at_index(2, 3), 3)

    def test_add_first(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.add_first(5), 5)

    def test_add_linked_list(self):
        ll_two = LinkedList()
        ll_two.add_element(6)
        ll_two.add_element(7)
        ll_two.add_element(8)
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.add_linked_list(ll_two), 8)

    def test_add_list(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        xs = [1, 2, 3]
        self.assertEqual(self.ll.add_list(xs), '5->6->7->1->2->3')

    def test_pop(self):
        self.ll.add_element(5)
        self.ll.add_element(6)
        self.ll.add_element(7)
        self.assertEqual(self.ll.pop(), 7)

    def test_reduce_to_unique(self):
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.add_element(7)
        self.assertEqual(self.ll.reduce_to_unique(), '5->7')

    def test_ll_from_to(self):
        self.ll.add_element(5)
        self.ll.add_element(5)
        self.ll.add_element(7)
        self.assertEqual(self.ll.ll_from_to(1, 2), '5->7')


if __name__ == '__main__':
    unittest.main()
