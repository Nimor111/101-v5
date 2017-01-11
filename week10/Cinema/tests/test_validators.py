import sqlite3
import unittest
from user_interface.validators import *
import database.create_database as dc
import database.modify_database as dm
import os


conn = sqlite3.connect('test.db')
dm.c = conn.cursor()
dc.c = conn.cursor()


class TestValidators(unittest.TestCase):

    def setUp(self):
        dc.create_database()
        dm.insert_user("Pesho", "123@123A2")

    def tearDown(self):
        dc.drop_database()

    @classmethod
    def tearDownClass(cls):
        os.remove('test.db')

    def test_validate_pass_works_on_valid_password(self):
        self.assertTrue(validate_pass("A@1231323"))

    def test_validate_pass_works_on_invalid_password(self):
        self.assertFalse(validate_pass("A1234567"))

    def test_check_user_works_on_existing(self):
        dm.insert_user("Pesho", "A@123454")
        self.assertEqual(check_user("Pesho"), "Pesho")


if __name__ == '__main__':
    unittest.main()
