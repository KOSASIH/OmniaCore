from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from .dashboard import dashboard
from .planet_profile import planet_profile

app.register_blueprint(dashboard)
app.register_blueprint(planet_profile)
