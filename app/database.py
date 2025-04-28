import json
import threading

db_lock = threading.Lock()

def read_database(db_path):
    with db_lock:
        with open(db_path, 'r') as db_file:
            return json.load(db_file)

def write_database(db_path, data):
    with db_lock:
        with open(db_path, 'w') as db_file:
            json.dump(data, db_file)
