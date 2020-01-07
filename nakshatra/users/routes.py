from flask import render_template, redirect, url_for, flash, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required
import string 
import random 

from nakshatra import db, bcrypt
from nakshatra.models import User, College_registration
from nakshatra.users.forms import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm, CollegeRegistrationForm
from nakshatra.users.utils import send_reset_email, send_generated_login

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, college=form.college.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Registered Successfuly', 'success')
        return redirect(url_for('main.home'))
    return render_template('users/register.html',form=form, title='Register')

@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Successful','success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email or password', 'danger')
    return render_template('users/login.html', form=form, title='Login')

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('users/reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/reset_token.html', title='Reset Password', form=form)

@users.route('/logout')
def logout():
    logout_user()
    flash('Logout Successful','success')
    return redirect(url_for('main.home'))


@users.route('/college_registration', methods=['GET', 'POST'])
def register_college():
    form = CollegeRegistrationForm()
    if form.validate_on_submit():
        new_reg = College_registration(college=form.college.data, leader_name=form.leader_name.data, leader_email=form.leader_email.data, part_1_name=form.participant_1_name.data, part_1_email=form.participant_1_email.data, part_2_name=form.participant_2_name.data, part_2_email=form.participant_2_email.data, part_3_name=form.participant_3_name.data, part_3_email=form.participant_3_email.data, part_4_name=form.participant_4_name.data, part_4_email=form.participant_4_email.data)
        db.session.add(new_reg)
        db.session.commit()
        gen_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        hashed_password = bcrypt.generate_password_hash(gen_password).decode('utf-8')
        user=User.query.filter_by(email=form.leader_email.data).first()
        if user:
            flash('Your leader or college already registered','danger')
            return render_template('users/college_registration.html', title='Register College', form=form)
        user = User(email=form.leader_email.data, college=form.college.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        send_generated_login(user,gen_password)
        flash('Your Registered Successfuly. Treasure Hunt username and password sent to leader\'s email', 'success')
        return redirect(url_for('main.home'))
    return render_template('users/college_registration.html', title='Register College', form=form)