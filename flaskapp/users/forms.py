from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import current_user
from flaskapp.models import User
from wtforms.validators import InputRequired, Email, Length,ValidationError

# LoginForm Class
# Describing how the validations should be
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

# RegisterForm Class
# Describing how the validations should be
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    
    # Username Validation
    def validate_username(self,username):
        user  = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username already taken")
        
    # Email Validation
    def validate_email(self,email):
        user  = User.query.filter_by(username = email.data).first()
        if user:
            raise ValidationError("Email already taken")