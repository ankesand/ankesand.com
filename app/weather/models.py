from app import db

class TownCity(db.Model):

    __bind_key__ = "towns_and_cities"
    __tablename__ = "towns_and_cities"

    name = db.Column("name", db.String(256), primary_key=True)
    town_or_city = db.Column("town_or_city", db.String(16))
    latitude = db.Column("latitude", db.String(20))
    longitude = db.Column("longitude", db.String(20))

    def __init__(self, name, town_or_city, latitude, longitude):

        self.name = name
        self.town_or_city = town_or_city
        self.latitude = latitude
        self.longitude = longitude
