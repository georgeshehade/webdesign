from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from vcwebsite.models import User
import sys
import os

class RegistrationForm(FlaskForm):

    # passwordfield needs better validators

    """
    RegistrationForm to register account content:
            -username           :'StringField length between 2/20'
            -email              :'StringField with email validator'
            -password           :'PasswordField with DataRequired (more coming soon)'
            -confirm_password   :'PasswordField '
    """
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one")


class LoginForm(FlaskForm):
    """
    Form for login to current_user, content:
            - email         :'Stringfield with email validator'
            - password      :'Stringfield with DataRequired'
            - remember      :'Boolean field to remember login info'
    """
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """
    Form to update your account info, content:
            - username      :'Stringfield with length between 2/20'
            - email         :'Stringfield with email validator'
    """
    username = StringField('Username',
                    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("that email is taken. Please choose a different one.")


class ValuesForm(FlaskForm):
    """Form for 3 string values checks if in list of /data/wordlist.txt"""
    if sys.platform.startswith('win'):
        with open('Value-Connection/source/vcwebsite_v1.1/vcwebsite/data/wordlist.txt', 'r') as wordlist:
            values = wordlist.read().splitlines()
    else:
        with open(os.getcwd() + '/vcwebsite/data/wordlist.txt', 'r') as wordlist:
            values = wordlist.read().splitlines()


    value1 = StringField('Value1', validators=[DataRequired()])
    value2 = StringField('Value2', validators=[DataRequired()])
    value3 = StringField('Value3', validators=[DataRequired()])
    submit = SubmitField("Use values")

    def validate_value1(self, value1):
        if value1.data not in self.values:
            raise ValidationError("Please select a valid value!")

    def validate_value2(self, value2):
        if value2.data not in self.values:
            raise ValidationError("Please select a valid value!")

    def validate_value3(self, value3):
        if value3.data not in self.values:
            raise ValidationError("Please select a valid value!")


class AdminForm(FlaskForm):
    """
    This class is a form class for admins and content can be accessed at administrator.py, the attributes are:
        - backup_db             :'Creates a backup of database'
        - create_db             :'Builds all database tables'
        - remove_db             :'Removes database completely from host'
        - drop_db               :'Drop all database tables'
        - train_cluster_model   :'Train clusters and store new cluster centroids'
        - update_user_clusters  :'Assign new cluster values to EACH user'
    """
    backup_db = BooleanField('Backup DB', validators=[])
    create_db = BooleanField('Create DB', validators=[])
    remove_db = BooleanField('Remove DB', validators=[])
    drop_db = BooleanField('Drop DB', validators=[])
    train_cluster_model = BooleanField('Train cluster model', validators=[])
    update_user_clusters = BooleanField('Update user clusters', validators=[])
    submit = SubmitField("Use")
