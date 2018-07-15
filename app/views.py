from flask import render_template, redirect, flash, url_for
from app import app
from .forms import LoginForm
from app.models import User
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
@app.route('/login', methods = ['GET','POST'])
def login():
    form  = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Username or Password is Wrong!")
            return redirect(url_for('login'))
        else:
            flash('Login successfull.! User {}'.format(form.username.data))
            return redirect('/dashboard')
    else:
        return render_template('login.html', title='Login', form = form)
@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html', title = 'Dashboard')