from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from a .env file into environment variables

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Load secret key from environment variables

# Example usage
DATABASE_PATH = os.getenv("DATABASE_PATH", "passwords.db")  # Default to 'passwords.db'
