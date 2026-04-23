from flask import Flask, request, render_template_string, jsonify
import sqlite3
import os

app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('id', '1')
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INT, name TEXT)')
    conn.execute("INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob')")
    query = f"SELECT name FROM users WHERE id = {user_id}"
    cursor = conn.execute(query)
    name = cursor.fetchone()
    return f"User name: {name[0] if name else 'not found'}"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return render_template_string(f"<h1>Hello {name}</h1>")

@app.route('/read')
def read_file():
    filename = request.args.get('file', '')
    with open(os.path.join('static', filename), 'r') as f:
        return f.read()

@app.route('/')
def index():
    return "DAST Test App"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)