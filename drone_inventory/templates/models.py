import email
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Patient(db.model):
    __tablename__ = "patients"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    facility = db.Column(db.String())
    unit = db.Column(db.String())

    def __init__(self, first_name, last_name, facility, unit):
        self.first_name = first_name
        self.last_name = last_name
        self.facility = facility
        self.unit = unit
