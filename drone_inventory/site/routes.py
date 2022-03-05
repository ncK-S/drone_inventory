from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='site_templates')

''' note that in the above code some arguments are specified 
the blueprint object the first argument sit is the blueprint's name'''

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')