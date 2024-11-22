from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Movie name',
        validators=[
            DataRequired(message='Manadatory field'),
            Length(1, 128)
        ]
    )
    text = TextAreaField(
        'Your opinion',
        validators=[
            DataRequired(message='Mandatory field')
        ]
    )
    source = URLField(
        'Link to moview review',
        validators=[
            Length(1, 256),
            Optional()
        ]
    )
    submit = SubmitField('Submit')
