from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug import secure_filename
from app import app, db
from .forms import LoginForm, RegisterForm
from app.models import User


@app.route('/')
@app.route('/home')
@login_required
def index():
    user = User.query.first()
    if user:
        user = user
    else:
        user = 'Guest'
    # user = 'Guest'
    return render_template('index.html', title='Home Page', user=user)


@app.route('/users')
@login_required
def users():
    userList = User.query.order_by(User.username).all()
    return render_template('users.html', title='Users Page', userList=userList)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Username or Password is Wrong!")
            return redirect(url_for('login'))
        login_user(user)
        
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data, email=form.email.data)
        mail = User.query.filter_by(email=form.email.data).first()
        username = User.query.filter_by(username=form.username.data).first()
        if mail is not None:
            flash('{} has been used!'.format(form.email.data))
            return render_template('register.html', title='Register', form=form)
        elif username is not None:
            flash('{} has been used!'.format(form.username.data))
            return render_template('register.html', title='Register', form=form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('{} has been added!'.format(form.email.data))
            return redirect(url_for('login'))
    else:
        return render_template('register.html', title='Register', form=form)


@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html', title='Dashboard')

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'