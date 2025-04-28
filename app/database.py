from flask import Blueprint, render_template, request, jsonify
from app.database import Database
from app.encryption import Encryption

main = Blueprint('main', __name__)
db = Database("passwords.db")
encryption = Encryption()

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/store', methods=['POST'])
def store_password():
    data = request.get_json()
    service = data['service']
    username = data['username']
    password = data['password']

    encrypted_password = encryption.encrypt(password)
    db.save(service, username, encrypted_password)
    return jsonify({"message": "Password stored successfully!"})

@main.route('/retrieve', methods=['POST'])
def retrieve_password():
    data = request.get_json()
    service = data['service']

    record = db.get(service)
    if record:
        decrypted_password = encryption.decrypt(record['password'])
        return jsonify({"username": record['username'], "password": decrypted_password})
    return jsonify({"error": "No credentials found for the requested service"}), 404
