import unittest
from tree import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(5)

    def test_init(self):
        self.assertEqual(self.tree.root.value, 5)

    def test_add_child(self):
        self.assertTrue(self.tree.add_child(5, 4))
        self.assertFalse(self.tree.add_child(6, 3))

    def test_find(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(4, 3)
        self.assertTrue(self.tree.find(4))
        self.assertFalse(self.tree.find(6))

    def test_height(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(4, 3)
        self.assertEqual(self.tree.height(), 2)

    def test_tree_levels(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(4, 3)
        self.assertEqual(self.tree.tree_levels(), [[5], [4], [3]])

    def test_DFS(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(4, 3)
        self.assertEqual(self.tree.DFS(self.tree.root), [5, 4, 3])


if __name__ == '__main__':
    unittest.main()
