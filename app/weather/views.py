from app import app
from app import db

from app import requests, json, datetime, pd

from app.weather.models import TownCity
from app.weather.forms import LatLong_TownCity

from flask import render_template, request, url_for, redirect

# weather - config

APIs = {
    "Global three hourly spot data" : {"three-hourly": "three-hourly"},
    "Global daily spot data": {"daily": "daily"},
    "Global hourly spot data": {"hourly": "hourly"}
    }

freq = "daily"

excludeParameterMetadata = "true" # N.B. lowercase string
includeLocationName = "true" # N.B. lowercase string

headers = {
    'x-ibm-client-id': app.config["MET_CLIENT_ID"],
    'x-ibm-client-secret': app.config["MET_CLIENT_SECRET"],
    'accept': "application/json"
    }

days_of_week = {0: "Mon",
                1: "Tues",
                2: "Weds",
                3: "Thurs",
                4: "Fri",
                5: "Sat",
                6: "Sun",
                }

@app.route("/work/weather2")
def weather2():

    towns_cities_autocomplete = [town_city.name for town_city in db.session.query(TownCity).all()]

    lat_long_town_city = LatLong_TownCity()

    title = "ankesand.com | work - weather"

    return render_template("weather/work-weather.html", towns_cities_autocomplete = towns_cities_autocomplete, lat_long_town_city = lat_long_town_city)

@app.route("/work/weather", methods=["GET", "POST"])
def weather():

    title = "weather (powered by Met Office 'DataPoint' (ankesand.com | work)"

    lat_long_town_city = LatLong_TownCity()

    towns_cities_autocomplete = [town_city.name for town_city in db.session.query(TownCity).all()]

    if lat_long_town_city.validate_on_submit():

        lat_ = db.session.query(TownCity).filter(TownCity.name == lat_long_town_city.town_city.data).one().latitude
        long_ = db.session.query(TownCity).filter(TownCity.name == lat_long_town_city.town_city.data).one().longitude

        url = "https://api-metoffice.apiconnect.ibmcloud.com/metoffice/production/v0/forecasts/point/{}?excludeParameterMetadata={}&includeLocationName={}&latitude={}&longitude={}".format(freq, excludeParameterMetadata, includeLocationName, lat_, long_)
        r = requests.get(url, headers=headers)

        json_data = json.loads(r.text)

        date, low, mid, high = [], [], [], []

        for tS in json_data["features"][0]["properties"]["timeSeries"][1:]:
            time = datetime.strptime(tS["time"], "%Y-%m-%dT%H:%MZ")
            date.append(days_of_week[time.weekday()] + " " + time.strftime("%d %b %Y"))
            low.append(tS["dayLowerBoundMaxTemp"])
            mid.append(tS["dayMaxScreenTemperature"])
            high.append(tS["dayUpperBoundMaxTemp"])

        location = json_data["features"][0]["properties"]["location"]["name"]

        forecast = pd.DataFrame({"Low": low, "Mid": mid, "High": high}, index = date)

        forecast = forecast.multiply({"Low": 2, "Mid": 2, "High": 2}).round({"Low": 0, "Mid": 0, "High": 0}).divide({"Low": 2, "Mid": 2, "High": 2})

        return render_template("weather/work-weather.html", title = title, lat_long_town_city = lat_long_town_city, towns_cities_autocomplete = towns_cities_autocomplete,
                lat_ = lat_, long_ = long_, location = location, forecast = forecast)

    return render_template("weather/work-weather.html", title = title, lat_long_town_city = lat_long_town_city, towns_cities_autocomplete = towns_cities_autocomplete)
