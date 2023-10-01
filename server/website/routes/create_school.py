from website import School, Location, db
from flask import Blueprint, request

bp = Blueprint("create_school", __name__, template_folder="routes")

@bp.route("/", methods=["POST"])
def create_school():
    json = request.get_json()
    school = School()
    school.name = json["general"]["name"]
    school.school_type = json["general"]["school_type"]
    location = Location()
    location.coordinates_ns = json["location"]["coordinates_ns"]
    location.coordinates_ew = json["location"]["coordinates_ew"]
    location.street = json["location"]["street"]
    location.street_number = json["location"]["street_number"]
    location.city = json["location"]["city"]
    school.location = location
    db.session.add(school)
    db.session.commit()
    return {
        "status": "OK"
    }