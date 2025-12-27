# Finance Tracker — Backend

A simple Python backend to track income, expenses, and balance using **SQLite** as the database.

---

## Features
- Add new transactions (credit / debit)
- Store data locally using SQLite
- Fetch all transactions
- Calculate total balance
- Easy to deploy & extend

---

## Tech Stack
- Python 3
- SQLite3

---
Setup:
1. Clone the repository:
   git clone https://github.com/akshithoudisetti-coder/finance-tracker---backend.git
   cd finance-tracker---backend

2. (Optional) Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate   (macOS / Linux)
   venv\Scripts\activate.bat  (Windows)

3. Install required dependencies:
   pip install -r requirements.txt

4. Initialize the database:
   python init_db.py

5. Run the application:
   python app.py

Project files:
app.py handles the main application logic. db.py manages database operations. init_db.py creates required tables. requirements.txt lists dependencies. .gitignore ensures database and virtual environment files are not committed.

This project is intended for learning, small personal use, or as a starting point for a more complete backend. You can modify or extend it as needed.
