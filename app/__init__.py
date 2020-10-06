from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import requests
import csv
import json

from datetime import datetime

from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy()

from wtforms import SelectMultipleField, widgets

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

from app.index import views
from app.weather import views
from app.rail import views

db.init_app(app)
