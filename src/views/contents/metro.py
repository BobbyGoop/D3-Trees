from flask import Blueprint, render_template

metro = Blueprint('metro', __name__)


@metro.route('/metro')
def show_page():
    return render_template('metro.html')