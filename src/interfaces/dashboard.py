from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def index():
    return render_template('dashboard.html')

@dashboard.route('/terraform')
def terraform():
    return render_template('terraform.html')
