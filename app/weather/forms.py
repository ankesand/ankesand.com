from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class LatLong_TownCity(FlaskForm):

    town_city = StringField("UK Town / City")
    submit = SubmitField("Submit", [InputRequired()])
