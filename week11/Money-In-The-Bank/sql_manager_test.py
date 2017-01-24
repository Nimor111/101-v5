import sys
import unittest
import os
import sql_manager
import sqlite3
import queries
import settings
from validators import validate_password, encode_pass

sys.path.append("..")

conn = sqlite3.connect(settings.TEST_DB_NAME)
sql_manager.cursor = conn.cursor()


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', 'AB@3232123')

    def tearDown(self):
        sql_manager.cursor.execute(queries.DROP_TABLE)

    @classmethod
    def tearDownClass(cls):
        os.remove(settings.TEST_DB_NAME)

    def test_validation(self):
        self.assertFalse(validate_password('Tester', '123'))
        self.assertFalse(validate_password('Zimbabwe', 'Zimbabwe@21'))
        self.assertTrue(validate_password('Tester', 'SDA@224FS2'))

    def test_register(self):
        sql_manager.register('Dinko', 'AB@3232123')

        sql_manager.cursor.execute(queries.COUNT_CLIENTS,
                                   ('Dinko', encode_pass('AB@3232123')))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', 'AB@3232123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123456@123A')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', 'AB@3232123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', 'AB@3232123')
        new_password = "AB@3232123"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')


if __name__ == '__main__':
    unittest.main()
