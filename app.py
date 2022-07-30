from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   send_file, session, url_for)
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 