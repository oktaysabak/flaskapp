from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db,login

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(70), unique = True)

    def set_password(self, password):
        self.password = password
    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False
@login.user_loader
def load_user(id):
    return User.query.get(int(id))