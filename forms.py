from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class PortfolioForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    bio = TextAreaField('Short Bio', validators=[DataRequired()])
    social_links = StringField('Social Media Links')
    projects = TextAreaField('Projects')
