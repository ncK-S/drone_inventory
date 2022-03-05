
from logging import root
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from config import Config
from .helpers import JSONEncoder
from .site.routes import site
from .api.routes import api

from .templates.models import db, Patient



app = Flask(__name__)
app.register_blueprint(site)
app.register_blueprint(api)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/create' , methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('profile.html')

app.run(host='localhost', port=5000)
# root_db.init_app(app)
# login_manager.init_app(app)
# login_manager.login_view = 'auth.signin' 
# # specify page rendered for non-authorized users ^
# ma.init_app(app)
# migrate = Migrate(app, root_db)

# CORS(app)
# app.json_encoder=JSONEncoder