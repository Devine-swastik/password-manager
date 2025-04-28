import json
import os

class Database:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump({}, file)

    def save(self, service, username, password):
        data = self._load_data()
        data[service] = {"username": username, "password": password}
        self._save_data(data)

    def get(self, service):
        data = self._load_data()
        return data.get(service)

    def _load_data(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
