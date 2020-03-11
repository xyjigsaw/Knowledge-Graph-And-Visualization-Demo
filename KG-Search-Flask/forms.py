from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
	BooleanField, PasswordField, DateField
from wtforms.validators import InputRequired, Email, Length, Optional, URL, Regexp


class KeywordSearchForm(FlaskForm):
	keyword = StringField("keyword", validators=[InputRequired(), Length(1,500)],description="搜索关键字，空格分开")