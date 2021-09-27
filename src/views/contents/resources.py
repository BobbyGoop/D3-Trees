from flask import Blueprint, render_template, send_file

resources = Blueprint('resources', __name__)


@resources.route('/resources/<resource_name>')
def show_page(resource_name):
    if resource_name == 'data.json':
        return send_file('static/js/data.json')