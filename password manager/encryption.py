from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self):
        key_file = "key.key"
        if not os.path.exists(key_file):
            key = Fernet.generate_key()
            with open(key_file, "wb") as file:
                file.write(key)
        else:
            with open(key_file, "rb") as file:
                key = file.read()
        return key

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        return self.cipher.decrypt(ciphertext.encode()).decode()
