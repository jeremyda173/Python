from flask import Flask, request
# from flask_sqlchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLLCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLLCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)