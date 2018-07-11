from flask import render_template
from app import app
from .forms import LoginForm
@app.route('/')
@app.route('/home')
def index():
    user = 'Guest'
    return render_template('index.html', title='H0me Page', user = user)
@app.route('/users')
def users():
    userList = [
        {'name':'Oktay', 'title':'Bonboşş Adam'},
        {'name':'Doğuş', 'title':'Daha Bonboşş Adam'},
    ]
    return render_template('users.html', title = 'Users Page', userList= userList)
@app.route('/login')
def login():
    form  = LoginForm()
    return render_template('login.html', title='Login', form = form)