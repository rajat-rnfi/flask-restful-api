from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

connection = os.getenv("DB_CONNECTION")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

app.config['SQLALCHEMY_DATABASE_URI'] = f"{connection}://{username}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)