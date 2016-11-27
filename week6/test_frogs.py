import unittest
from frogs import *


class FrogTest(unittest.TestCase):

    def setUp(self):
        self.frog = FrogTree(">>>_<<<")

    def test_get_combs(self):
        self.assertEqual(self.frog.get_root_combs(self.frog.tree.root()),
                         [">>_><<<", ">_>><<<", ">>><_<<", ">>><<_<"])

    def test_get_current_combs(self):
        self.frog.get_root_combs(self.frog.tree.root())
        self.assertEqual(self.frog.get_current_combs(),
                         [">>_><<<", ">_>><<<", ">>><_<<", ">>><<_<"])


if __name__ == '__main__':
    unittest.main()
