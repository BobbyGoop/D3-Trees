from flask import Blueprint, render_template

register = Blueprint('register', __name__)


@register.route('/register')
def show_page():
    return render_template('register.html')