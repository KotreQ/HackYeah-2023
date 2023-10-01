from flask import Flask
from . import config
from .db import db
from .models import School, FieldOfStudy, Location  # needs to be loaded earlier
import os
import website
from sqlalchemy.exc import OperationalError


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQL_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def register_blueprints(app, blueprints_module_name):
    blueprints_path = os.path.join(
        os.path.dirname(website.__file__), blueprints_module_name
    )

    for root, _, files in os.walk(blueprints_path):
        for file in files:
            if file == "__init__.py" or not file.endswith(".py"):
                continue

            blueprint_name = os.path.splitext(file)[0]

            blueprint_reldir = os.path.relpath(root, blueprints_path).replace("\\", "/")
            if blueprint_reldir == ".":
                blueprint_reldir = ""

            blueprint_module = (
                f"{blueprints_module_name}.{blueprint_reldir}.{blueprint_name}"
            )

            blueprint_module = (
                f"{blueprints_module_name}.{blueprint_reldir.replace('/', '.')}.{blueprint_name}"
                if blueprint_reldir
                else f"{blueprints_module_name}.{blueprint_name}"
            )

            blueprint_module = f"{__name__}.{blueprint_module}"

            blueprint = getattr(__import__(blueprint_module, fromlist=["bp"]), "bp")

            url_prefix = (
                f"{f'/{blueprint_reldir}' if blueprint_reldir else ''}/{blueprint_name}"
            )

            app.register_blueprint(
                blueprint,
                url_prefix=url_prefix,
            )


register_blueprints(app, "routes")


with app.app_context():
    db.init_app(app)
    try:
        db.create_all()
    except OperationalError:
        raise ValueError(
            f"Cannot connect to the specified database: {config.SQL_DATABASE_URI}"
        )
