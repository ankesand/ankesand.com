from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from wtforms.validators import InputRequired

class Station_CRS(FlaskForm):

    crs = StringField("Station (CRS)", validators=[InputRequired()])
    submit = SubmitField("Submit", validators=[InputRequired()])
