import os
from flask import Flask
from flask_restful import Api
from src.views.contents.routes import initialise_contents
from src.views.api.routes import initialise_resources
from src.database.setup import initialise_db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app._static_folder = os.path.abspath("src/static/")

api = Api(app)

if __name__ == '__main__':
    initialise_db(app)
    initialise_contents(app)
    initialise_resources(api)
    app.run(debug=True)

#
# @app.route('/')
# def hello_world():
#     return render_template("index.html", title="Главная")
#
#
# @app.route('/tree-binary')
# def binary_tree():
#     return render_template("tree.html", title="Бинарное дерево")
#
#
# @app.route('/graph')
# def graph():
#     return render_template("metro.html", title="Бинарное дерево")
#
#
#
#
#
# @app.route('/register')
# def register():
#     return render_template("register.html", title="Регистрация")



