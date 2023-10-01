from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

school_and_field = db.Table(
    "school_field",
    db.Column("school_id", db.Integer, db.ForeignKey("school.id")),
    db.Column("field_of_study_id", db.Integer, db.ForeignKey("field_of_study.id"))
)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), unique=True)
    school_type = db.Column(db.String(40))
    location = db.relationship("Location", backref="school")

class FieldOfStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(300))
    schools = db.relationship("School", secondary=school_and_field, backref="school")

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.Integer, db.ForeignKey("field_of_study.id"), nullable=False, unique=True)
    city = db.Column(db.String(30))
    street = db.Column(db.String(30))
    street_number = db.Column(db.Integer)
    coordinates_ns = db.Column(db.String(30))
    coordinates_ew = db.Column(db.String(30))