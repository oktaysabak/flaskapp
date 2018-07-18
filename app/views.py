from flask import render_template, redirect, flash, url_for
from app import app, db
from .forms import LoginForm, RegisterForm
from app.models import User
@app.route('/')
@app.route('/home')
def index():
    user = 'Guest'
    return render_template('index.html', title='H0me Page', user = user)
@app.route('/users')
def users():
    userList = User.query.order_by(User.username).all()
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
@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user  = User(username=form.username.data, password = form.password.data, email = form.email.data)
        mail = User.query.filter_by(email=form.email.data).first()
        if mail is not None:
            flash('{} has been used!'.format(form.email.data))
            return render_template('register.html', title = 'Register', form = form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('{} has been added!'.format(form.email.data))
            return redirect(url_for('login'))
    else:
        return render_template('register.html', title = 'Register', form = form)
@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html', title = 'Dashboard')