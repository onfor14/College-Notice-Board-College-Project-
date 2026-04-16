from flask import Flask, request, jsonify, session
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
app.secret_key = 'college_secret_key'

# 🔥 IMPORTANT: CORS FIX
CORS(app, supports_credentials=True)

# 🔷 Database Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # your username
        password="mysql",           # your password
        database="college_notice_board"
    )

# 🔷 LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user:
        session['user_id'] = user['id']
        session['role'] = user['role']

        return jsonify({
            "success": True,
            "role": user['role']
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


# 🔷 GET NOTICES
@app.route('/notices', methods=['GET'])
def get_notices():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM notices ORDER BY date_added DESC")
    notices = cursor.fetchall()

    cursor.close()
    db.close()

    for n in notices:
        n['date_added'] = str(n['date_added'])
        n['last_date'] = str(n['last_date'])

    return jsonify(notices)


# 🔷 ADD NOTICE
@app.route('/add-notice', methods=['POST'])
def add_notice():
    if session.get('role') != 'admin':
        return jsonify({"success": False, "message": "Unauthorized"}), 403

    data = request.json

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO notices (title, description, category, date_added, last_date) VALUES (%s, %s, %s, %s, %s)",
        (
            data['title'],
            data['description'],
            data['category'],
            data['date_added'],
            data['last_date']
        )
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"success": True})


# 🔷 LOGOUT
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"success": True})


# 🔷 RUN
if __name__ == '__main__':
    app.run(debug=True, port=5000)