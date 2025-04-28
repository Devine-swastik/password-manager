from password_manager.database import Database
from password_manager.encryption import Encryption

class PasswordManager:
    def __init__(self):
        self.db = Database("passwords.db")
        self.encryption = Encryption()

    def store_password(self, service, username, password):
        encrypted_password = self.encryption.encrypt(password)
        self.db.save(service, username, encrypted_password)

    def retrieve_password(self, service):
        record = self.db.get(service)
        if record:
            decrypted_password = self.encryption.decrypt(record['password'])
            return {"username": record['username'], "password": decrypted_password}
        return None
