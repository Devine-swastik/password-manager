# Password Manager

A secure password manager built with Flask.

## Features
- Encrypt and store passwords
- Simple and intuitive UI
- Lightweight and fast

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Devine-swastik/password-manager.git
   cd password-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_PATH=path/to/passwords.db
   ```

5. Run the app:
   ```bash
   flask run
   ```

## Testing
Run unit tests:
```bash
python -m unittest discover
```

## Deployment
Deploy to Heroku:
```bash
git push heroku main
```
