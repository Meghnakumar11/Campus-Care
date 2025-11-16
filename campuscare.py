# app.py
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "campus-care-key")
CORS(app)
DB_NAME = "database.db"

def get_db_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    rollno= data.get("rollno")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not rollno or not password:
        return jsonify({"error": "Please fill all fields"})

    hashed_pass = generate_password_hash(password)
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, rollno, email, password_hash) VALUES (?, ?, ?, ?)",
            (username, rollno, email, hashed_pass)
        )
        connection.commit()
        return jsonify({"message": "Signup successful!"})
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username or email already taken"})
    finally:
        connection.close()



@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username_or_email_or_rollno = data.get("username_or_email_or_rollno")
    password = data.get("password")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? OR email = ? OR rollno = ?",
        (username_or_email_or_rollno, username_or_email_or_rollno, username_or_email_or_rollno)
    )
    user = cursor.fetchone()
    connection.close()

    if user and check_password_hash(user["password_hash"], password):
        session["user_id"]=user["id"]
        session["username"]=user["username"]
        return jsonify({"message": "Login successful!"})

    else:
        return jsonify({"error": "Invalid username or password"})



@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully!"})



@app.route("/feedback", methods=["POST"])
def feedback():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Please login first"})

    data = request.get_json()
    msg = data.get("message")
    
    if not msg:
        return jsonify({"error": "Feedback message is required"})

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO feedback (user_id, message) VALUES (?, ?)",
        (user_id, msg)
    )
    connection.commit()
    connection.close()
    return jsonify({"message": "Feedback submitted successfully!"})



@app.route("/myfeedback", methods=["GET"])
def my_feedback():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Please login first"})

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, message, created_at FROM feedback WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    rows = cursor.fetchall()
    connection.close()

    feedback_list = [dict(row) for row in rows]
    return jsonify({"feedback": feedback_list})



@app.route("/consultation", methods=["POST"])
def consultation():
    data = request.get_json()
    name = data.get("name")
    rollno = data.get("rollno")
    email = data.get("email")
    service = data.get("service")
    message = data.get("message")

    if not name or not rollno or not email or not service or not message:
        return jsonify({"error": "All fields are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO consultations (name, rollno, email, service, message) VALUES (?, ?, ?, ?, ?)",
            (name, rollno, email, service, message)
        )
        connection.commit()
        return jsonify({"message": "Consultation request submitted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()



@app.route("/consultations", methods=["GET"])
def get_consultations():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, rollno, email, service, message, status, created_at FROM consultations ORDER BY created_at DESC"
    )
    rows = cursor.fetchall()
    connection.close()

    consultations_list = [dict(row) for row in rows]
    return jsonify({"consultations": consultations_list})



if __name__ == "__main__":
    print("Starting Campus Care backend server...")
    app.run(debug=True)
