from app import app
from app import db

from app import requests, bs, csv

# from app.rail.models import _
from app.rail.forms import Station_CRS

from flask import render_template

# rail - config

from darwin import *

# station_codes_url = "https://www.nationalrail.co.uk/static/documents/content/station_codes.csv"

station_codes_url = "https://www.nationalrail.co.uk/stations_destinations/48541.aspx"
station_codes_response = requests.get(station_codes_url)
station_codes_soup = bs(station_codes_response.text, "lxml")
# station_codes = csv.DictReader(station_codes_response.text.splitlines())
# station_codes_crs = {row["CRS Code"]: row["Station Name"] for row in station_codes}
station_codes_crs = {}
for tr in station_codes_soup.find_all("table")[-1].find("tbody").find_all("tr")[1:]:
        station_codes_crs[tr.find_all("td")[1].text] = tr.find_all("td")[0].text
# station_codes = csv.DictReader(station_codes_response.text.splitlines())
# station_codes_stations = {row["Station Name"]: row["CRS Code"] for row in station_codes}
station_codes_stations = {}
for tr in station_codes_soup.find_all("table")[-1].find("tbody").find_all("tr")[1:]:
        station_codes_stations[tr.find_all("td")[0].text] = tr.find_all("td")[1].text

@app.route("/work/rail", methods=["GET", "POST"])
def rail():

    title = "rail (ankesand.com | work)"

    station_crs = Station_CRS()
#    station_crs.crs.choices = [(i, i) for i in station_codes_stations]
    stations = [station for station in station_codes_stations]

    raildepartures = "here's some rail departures: rd1, rd2, rd3"
#    railservices = "here's some rail services: rs1, rs2, rs3"
    railservices = None

    if station_crs.validate_on_submit():

        station = station_crs.crs.data
        crs = station_codes_stations[station]
        departures = get_departures(crs)

        return render_template("rail/work-rail.html", title = title, stations = stations, station_crs = station_crs, crs = crs, station = station, departures = departures)

    return render_template("rail/work-rail.html", title = title, stations = stations, station_crs = station_crs, raildepartures = raildepartures)#, railservices = railservices)

@app.route("/work/rail/code", methods=["GET", "POST"])
def rail_code():

    title = "rail (ankesand.com | work)"

    return render_template("rail/work-rail-code.html", title = title)
