from flask_restful import Resource, Api, reqparse
from flask import Flask, render_template, request, redirect, url_for, jsonify
from db_setup import db_session, init_db
from db_models import *
import os

app = Flask(__name__)
api = Api(app)
app._static_folder = os.path.abspath("templates/static/")

parser = reqparse.RequestParser()
parser.add_argument('client_id', type=int, help="Enter the client id")
parser.add_argument('order_id', type=int, help="Enter the client id")


# jsonify расставляет атрибуты по алфавиту
class ClientsList(Resource):
    def __init__(self):
        self._cid = parser.parse_args().get('client_id')

    def get(self):
        if self._cid:
            return jsonify(db_session.query(Client).get(self._cid).serialize())
        else:
            return {"clients": list(map(lambda cl: cl.serialize(), db_session.query(Client).all()))}


class OrdersList(Resource):
    def __init__(self):
        self._cid = parser.parse_args().get('client_id')
        self._oid = parser.parse_args().get('order_id')

    def get(self):
        if not self._cid and not self._oid:
            return {'orders': list(map(lambda cl: cl.serialize(), Order.query.all()))}
        elif self._cid and self._oid:
            ordr = db_session.query(Order).get(self._oid)
            return jsonify(ordr.serialize()) if ordr.client_id == self._cid else 404
        elif self._cid and not self._oid:
            return list(map(lambda o: o.serialize(), filter(lambda o: o.client_id == self._cid, db_session.query(Order).all())))


api.add_resource(ClientsList, '/clients/')
api.add_resource(OrdersList, '/orders/')


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
    return render_template("layouts/register.html", title="Регистрация")


@app.teardown_appcontext
def shutdown_session(exception = None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
