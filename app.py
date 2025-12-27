from flask import Flask, jsonify, request
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Finance Tracker API is running"})

@app.route("/expenses", methods=["GET"])
def get_expenses():
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return jsonify([dict(row) for row in expenses])

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
        (data["amount"], data["category"], data["description"])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Expense added"}), 201


@app.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Expense deleted"})

if __name__ == "__main__":
    app.run(debug=True)