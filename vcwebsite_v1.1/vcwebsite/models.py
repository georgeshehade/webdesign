from vcwebsite import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask_wtf import FlaskForm
# import FlaskForm
from wtforms import SubmitField
from sqlalchemy_utils import ScalarListType

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    User class database initialization,
    creates User table in sql
    content:
            -id             :'Integer primary_key=True'
            -username       :'String size=20, unique=True, nullable=False'
            -email          :'String size=120, unique=True, nullable=False'
            -password       :'String size=60, nullable=False'
            -cluster        :'Integer nullable=True'
            
        ::datapoints might need changes in future to make it more generalized
            -datapoint1     :'Float nullable=True'
            -datapoint2     :'Float nullable=True'
            -datapoint3     :'Float nullable=True'
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cluster = db.Column(db.Integer, nullable=True)
    
    # datapoint part might need to be generalized so every size is possible
    datapoint1 = db.Column(db.Float, nullable=True)
    datapoint2 = db.Column(db.Float, nullable=True)
    datapoint3 = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Values(db.Model):
    """
    Values class database initialization,
    creates Values table in sql
    content:
            -id             :'Integer primary_key=True'
            -comp_name      :'String size=100 nullable=True'
            -value1         :'String size=100 nullable=False'
            -value2         :'String size=100 nullable=False'
            -value3         :'String size=100 nullable=False'
    """
    id = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(100), nullable=True)
    value1 = db.Column(db.String(100), nullable=False)
    value2 = db.Column(db.String(100), nullable=False)
    value3 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Values({self.comp_name}, {self.value1}, {self.value2}, {self.value3})"

