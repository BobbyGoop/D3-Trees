from flask_restful import Api
from flask import Flask, render_template, request, redirect, url_for
from api import ClientWrapper, OrderWrapper
from db_setup import db_session, init_db
import os

app = Flask(__name__)
api = Api(app)
app._static_folder = os.path.abspath("templates/static/")

api.add_resource(ClientWrapper, '/api/clients/')
api.add_resource(OrderWrapper, '/api/orders/')


@app.route('/')
def hello_world():
    return render_template("layouts/index.html", title="Главная")


@app.route('/tree-binary')
def binary_tree():
    return render_template("layouts/binary.html", title="Бинарное дерево")


@app.route('/graph')
def graph():
    return render_template("layouts/graph.html", title="Бинарное дерево")


@app.route('/tree-dynamic')
def dynamic_tree():
    return render_template("layouts/dynamic.html", title="Бинарное дерево")


@app.route('/register')
def register():
    return render_template("layouts/register.html", title="Регистрация")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
