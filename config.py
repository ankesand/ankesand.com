MAIL_FROM_EMAIL = "no-reply@ankesand.com"

user = "[secret]"
password = "[secret]"
mysqldb = "db1"

SQLALCHEMY_DATABASE_URI = "mysql://" + user + ":" + password + "@127.0.0.1/" + mysqldb

SQLALCHEMY_BINDS = {"db1": "mysql://" + "sqladmin" + ":" + password + "@127.0.0.1/" + "db1",
                    "urls": "mysql://" + "sqladmin" + ":" + password + "@127.0.0.1/" + "anks_co_urls",
                    "ankesand_users": "mysql://" + "sqladmin" + ":" + password + "@127.0.0.1/" + "ankesand_users",
                    "towns_and_cities": "mysql://" + user + ":" + password + "@127.0.0.1/" + "towns_and_cities",
                    "products":  "mysql://" + user + ":" + password + "@127.0.0.1/" + "product_demo"
                                  }
SECRET_KEY = "[secret]"

# MetCheck

MET_CLIENT_ID = "[secret]"
MET_CLIENT_SECRET = "[secret]"
