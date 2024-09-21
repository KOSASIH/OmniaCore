from flask import Blueprint, render_template

planet_profile = Blueprint('planet_profile', __name__)

@planet_profile.route('/planets/<string:planet_id>')
def planet_profile(planet_id):
    # Retrieve planetary data from database
    planet_data = {"name": "Kepler-62f", "classification": "Terrestrial"}
    return render_template('planet_profile.html', planet_data=planet_data)
