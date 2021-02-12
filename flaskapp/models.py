from flask import current_app
from flaskapp import login_manager
from flaskapp import db 
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


# Flask Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User database class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

