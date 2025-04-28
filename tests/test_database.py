import unittest
import os
from password_manager.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_file = "test_passwords.db"
        self.database = Database(self.db_file)

    def tearDown(self):
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_save_and_get(self):
        self.database.save("TestService", "test_user", "encrypted_password")
        record = self.database.get("TestService")
        self.assertEqual(record["username"], "test_user")
        self.assertEqual(record["password"], "encrypted_password")

    def test_get_nonexistent_service(self):
        record = self.database.get("NonExistentService")
        self.assertIsNone(record)
