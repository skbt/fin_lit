import email
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   send_file, session, url_for)
from dotenv import load_dotenv
from numpy import roll
from passlib.hash import pbkdf2_sha256 as sha256
from models import *
import os

load_dotenv()

INIT_DP = "https://res.cloudinary.com/dtvhyzofv/image/upload/v1647144583/banter/dp/user_awjxuf.png"

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
db = db_init(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/login')
def login_page():
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login_user():
    login_creds = request.form.to_dict()
    if login_creds['id'] == '' or login_creds['pass'] == '':
        flash('Please enter a username and password')
        return redirect(url_for('login_page'))
    else:
        user = User.query.filter_by(id=login_creds['id']).first()
        if user and sha256.verify(login_creds['pass'], user.password):
            # user_roles = UserRoles.query.filter_by(student_id=user.id).all()
            # roles = [role.role_id for role in user_roles]
            # session['user_roles'] = roles
            # print(f'User Roles ==> {roles}')
            session['user'] = user.format()
            flash('Welcome back, {}!'.format(session['user']['name']))
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password')
            return redirect(url_for('login_page'))

@app.route('/register')
def register():
    if 'user' not in session:
        return render_template('login/register.html')
    else:
        return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register_user():
    if 'user' not in session:
        name = request.form['name']
        school_id = request.form['school_id']
        school_name = request.form['school_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Passwords do not match!')
            return redirect(url_for('register'))
        else:
            try:
                new_user = User(id=school_id, name=name, password=sha256.hash(
                    password), school=school_name, email="", major="", phone="", dp=INIT_DP, role_id=1)
                new_user.insert()
                session['user'] = new_user.format()
                flash("Welcome to your best campus life, {}!".format(
                    session['user']['name']))
                return redirect(url_for('home'))
            except Exception as e:
                print(f'Error ==> {e}')
                flash('Something went wrong!')
                return redirect(url_for('register'))
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Remove the user from session
    if 'user' in session:
        session.pop('user')
        if 'user_roles' in session:
            session.pop('user_roles')
    if 'broadcast_messages' in session:
        session.pop('broadcast_messages')
    return redirect(url_for('home'))

@app.route('/course')
def course():
    modules = Modules.query.all()
    return render_template('course.html', modules=modules)

@app.route('/modules/<int:module_id>')
def module(module_id):
    if 'user' not in session:
        flash('Please login to start the course!')
        return redirect(request.referrer)
    submodules = SubModules.query.filter_by(module_id=module_id).all()
    quizzes = ModuleQuiz.query.filter_by(module_id=module_id).all()
    return render_template('module.html', module_id=module_id, submodules=submodules, quizzes=quizzes)

@app.route('/quiz/<id>')
def quiz(id):
    quiz = ModuleQuiz.query.filter_by(id=id).first()
    return render_template(f'quiz/{quiz.file_name}.html', quiz=quiz)

@app.route('/workbook/<id>')
def workbook(id):
    quiz = ModuleQuiz.query.filter_by(id=id).first()
    return render_template(f'quiz/{quiz.file_name}.html', quiz=quiz)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 