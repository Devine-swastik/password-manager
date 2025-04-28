import unittest
from password_manager.encryption import Encryption

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.encryption = Encryption()

    def test_encrypt_and_decrypt(self):
        plaintext = "test_password"
        encrypted = self.encryption.encrypt(plaintext)
        decrypted = self.encryption.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_different_encrypted_values_for_same_input(self):
        plaintext = "test_password"
        encrypted1 = self.encryption.encrypt(plaintext)
        encrypted2 = self.encryption.encrypt(plaintext)
        self.assertNotEqual(encrypted1, encrypted2)
