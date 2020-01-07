from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import StringField, SelectField, PasswordField, SubmitField, BooleanField

from nakshatra.models import User, College_registration

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=60)])
    college = SelectField('College', choices=[('nitc','NITC'),('nitt','NITT'),('nits','NITS')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        emailid = User.query.filter_by(email=email.data).first()
        if emailid:
            raise ValidationError('Already registered')
    
    def validate_college(self, college):
        college_name = User.query.filter_by(college=college.data).first()
        if college_name:
            raise ValidationError('Your College is already registered')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class CollegeRegistrationForm(FlaskForm):
    college = SelectField('College', choices=[('nitc','NITC'),('nitt','NITT'),('nits','NITS')])
    leader_name = StringField('Leader Name', validators=[DataRequired(),Length(min=3,max=40)],render_kw={"placeholder": "Name"})
    leader_email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    participant_1_name = StringField('Participant 1 Name', validators=[DataRequired(),Length(min=3,max=40)],render_kw={"placeholder": "Name"})
    participant_1_email = StringField('Participant 1 Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    participant_2_name = StringField('Participant 1 Name', validators=[DataRequired(),Length(min=3,max=40)],render_kw={"placeholder": "Name"})
    participant_2_email = StringField('Participant 1 Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    participant_3_name = StringField('Participant 1 Name', validators=[DataRequired(),Length(min=3,max=40)],render_kw={"placeholder": "Name"})
    participant_3_email = StringField('Participant 1 Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    participant_4_name = StringField('Participant 1 Name', validators=[DataRequired(),Length(min=3,max=40)],render_kw={"placeholder": "Name"})
    participant_4_email = StringField('Participant 1 Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    submit = SubmitField('Register')

    def validate_leader_email(self, email):
        reg = College_registration.query.filter_by(leader_email=email.data).first()
        if reg:
            raise ValidationError('Already Registered with same leader email')
    
    def validate_college(self, college):
        reg  = College_registration.query.filter_by(college=college.data).first()
        if reg:
            raise ValidationError('Already Registered with this college')