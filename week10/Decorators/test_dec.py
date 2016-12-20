import unittest
from decos import accepts


class TestDec(unittest.TestCase):

    def setUp(self):
        pass

    def test_raises_exception_with_non_string_argument(self):

        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        self.assertRaises(TypeError, say_hello, 4)

    def test_correct_output_with_string_argument(self):

        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        self.assertEqual(say_hello('Georgi'), "Hello, I am Georgi")


if __name__ == '__main__':
    unittest.main()
