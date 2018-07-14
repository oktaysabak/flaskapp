from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)