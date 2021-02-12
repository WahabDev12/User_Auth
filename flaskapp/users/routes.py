from flask import render_template, url_for, flash, redirect, request, Blueprint,session
from flask_login import login_user, current_user, logout_user, login_required
from flaskapp import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flaskapp.models import User
from flaskapp.users.forms import RegisterForm, LoginForm

# Creating an instance for users Blueprint
users = Blueprint("users",__name__,static_folder="static",template_folder="templates",url_prefix="/student")

# SIGNUP ROUTE
@users.route('/signup', methods=['GET', 'POST'])
def signup():
    # Creating an instance for registration form
    form = RegisterForm()

    if form.validate_on_submit():
        # Hash user password into string format on form submission
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        #Add user to database
        db.session.add(new_user)
        db.session.commit()
        
        # Redirect to login page
        return redirect(url_for("users.login"))

    return render_template('signup.html', form=form)

# LOGIN ROUTE
@users.route('/login', methods=['GET', 'POST'])
def login():
    # Create instance for LoginForm
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # Check if user password equals hashed password when loggin in
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)   
                # Redirect to dashboard
                return redirect(url_for('users.dashboard'))
        else:
            # Return a flash message if user password is incorrect
            flash("Invalid username or password","danger")

    return render_template('login.html', form=form)

# DASHBOARD ROUTE
@users.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

#LOGOUT ROUTE
@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.signup'))