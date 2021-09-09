from flask_restful import Resource, Api
from flask import Flask, render_template, request, redirect, url_for, jsonify
from db_setup import db_session, init_db
from db_models import *
import os

app = Flask(__name__)
api = Api(app)
app._static_folder = os.path.abspath("templates/static/")


class ClientList(Resource):
    def get(self):
        return jsonify({'clients': list(map(lambda cl: cl.serialize(), Client.query.all()))})


api.add_resource(ClientList, '/clients')


@app.route('/')
def hello_world():
    return render_template("layouts/index.html", title = "Главная")


@app.route('/tree-binary')
def binary_tree():
    return render_template("layouts/binary.html", title = "Бинарное дерево")


@app.route('/graph')
def graph():
    return render_template("layouts/graph.html", title = "Бинарное дерево")


@app.route('/tree-dynamic')
def dynamic_tree():
    return render_template("layouts/dynamic.html", title = "Бинарное дерево")


@app.route('/register', methods=("POST", "GET"))
def register():
    if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
        try:
            c = Client(request.form['name'], request.form['surname'], request.form['email'])
            db_session.add(c)
            db_session.flush()

            o = Order(c.id, c.name, 0)
            db_session.add(o)
            db_session.commit()
            print("Добавлено")
        except:
            db_session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('register'))
    print(Client.query.all())
    print(db_session.query(Order))
    return render_template("layouts/register.html", title = "Регистрация")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()

    # client = Client("Client 1","Surname 1","123@mail.ru")
    # print(Client.id)
    # order = Order(datetime.now(), Client.id)
    # db_session.add(client, order)
    # db_session.commit()
    app.run(debug=True)
