from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20), unique=False)

    def __init__(self, attrs):
        for key in attrs:
            setattr(self, key, attrs[key])

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return '<User %r>' % self.username

class PublicKey(db.Model):
    __tablename__ = "public_key"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    content = db.Column(db.String(3000), unique=False)
    category_id = db.Column(db.Integer, db.ForeignKey('public_key_category.id')) 
    def __init__(self, attrs):
        for key in attrs:
            setattr(self, key, attrs[key])

    def __repr__(self):
        return '<PublicKey %r>' % self.title

    def __str__(self):
        return '<PublicKey %r>' % self.title

class PublicKeyCategory(db.Model):
    __tablename__ = "public_key_category"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, attrs):
        for key in attrs:
            setattr(self, key, attrs[key])

    def __repr__(self):
        return '<PublicKeyCategory %r>' % self.title

    def __str__(self):
        return '<PublicKeyCategory %r>' % self.title
