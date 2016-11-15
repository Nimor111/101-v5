import unittest
from reduce_file_path import *


class TestReduce(unittest.TestCase):

    def setUp(self):
        self.path = "/srv/www/htdocs/wtf"

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path(self.path), "/srv/www/htdocs/wtf")


if __name__ == "__main__":
    unittest.main()
