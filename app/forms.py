from flask_wtf import FlaskForm
from wtforms.fields import TextField,TextAreaField,SelectField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname =TextField('Firstname', validators=[DataRequired()])
    lastname =TextField('Lastname', validators=[DataRequired()]) 
    gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    email=TextField('Email', validators=[DataRequired(), Email()]) 
    location=TextField('Location',validators=[DataRequired()])
    biography=TextAreaField('Bio',validators=[DataRequired()])
    fileupload=FileField(validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    