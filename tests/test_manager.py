import unittest
from password_manager.manager import PasswordManager

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.manager = PasswordManager()

    def test_store_and_retrieve_password(self):
        self.manager.store_password("TestService", "test_user", "test_password")
        credentials = self.manager.retrieve_password("TestService")
        self.assertEqual(credentials["username"], "test_user")
        self.assertEqual(credentials["password"], "test_password")
