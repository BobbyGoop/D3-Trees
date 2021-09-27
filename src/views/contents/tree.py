from flask import Blueprint, render_template

tree = Blueprint('tree', __name__)


@tree.route('/tree')
def show_page():
    return render_template('tree.html')