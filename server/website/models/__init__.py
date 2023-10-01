from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    school_type = db.Column(db.String)
    coordinates = db.Column(db.String)
