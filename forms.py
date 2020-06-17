 
from flask_wtf import FlaskForm

from wtforms  import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,Email,EqualTo


class RegistrationForm(FlaskForm):

	firstname = StringField('First name', validators=[DataRequired() ])

	lastname = StringField('Last name', validators=[DataRequired() ])

	username = StringField('Username', validators=[DataRequired() ])


	email = StringField('Email', validators=[DataRequired(),Email()] )

	password = PasswordField('Password', validators=[DataRequired()] )

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)] )

	submit= SubmitField('Sign Up')




class LoginForm(FlaskForm):

	username = StringField('Username', validators=[DataRequired(),length(min=2,max=20) ])

	email = StringField('Email', validators=[DataRequired(),Email()] )

	password = PasswordField('Password', validators=[DataRequired()] )
	

	remember = BooleanField('Remember Me')
	submit= SubmitField('Login')






