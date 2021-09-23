import os
from flask import Flask, render_template, send_file
from flask_restful import Api
from db_setup import db
from api import ClientWrapper, OrderWrapper


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app._static_folder = os.path.abspath("templates/static/")


api = Api(app)
api.add_resource(ClientWrapper, '/api/clients/', '/api/clients/<int:client_id>')
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


@app.route('/resources/<resource_name>')
def resources(resource_name):
    if resource_name == 'data.json':
        return send_file('./templates/static/js/data.json')


@app.route('/register')
def register():
    return render_template("layouts/register.html", title="Регистрация")


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
