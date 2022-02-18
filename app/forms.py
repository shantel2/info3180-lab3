from email import message
from tkinter.tix import Form
from flask_wtf import Form

from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class contactForm(Form):
    #name, email, subject and a text area for a message.
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])








