from flask import Flask, request, render_template_string, jsonify
import sqlite3
import os

app = Flask(__name__)



@app.route('/')
def index():
    return "DAST Test App"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)