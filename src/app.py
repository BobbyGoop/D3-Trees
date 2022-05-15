import os
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager

from src.database.models.TokenBlocklist import TokenBlocklist
from src.database.setup import db

from src.views.api.ClientWrapper import ClientWrapper
from src.views.api.OrderWrapper import OrderWrapper
from src.views.api.LoginWrapper import LoginWrapper
from src.views.api.LogoutWrapper import LogoutWrapper

from src.views.contents.home import home
from src.views.contents.metro import metro
from src.views.contents.resources import resources
from src.views.contents.tree import tree

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = '2efbc2bd1b15462081b981dd4f83070d'
app._static_folder = os.path.abspath("../src/static/")

api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


@app.route('/labs/part-one')
def show_page_1():
    return render_template('lab1_base.html')


@app.route('/labs/part-two')
def show_page_2():
    return render_template('lab2_text.html')


@app.route('/labs/part-three')
def show_page_3():
    return render_template('lab3_table.html')


@app.route('/labs/part-four')
def show_page_4():
    return render_template('lab4_form.html')


@app.route('/labs/part-five')
def show_page_5():
    return render_template('lab5_flex.html')


@app.route('/labs/part-six')
def show_page_6():
    return render_template('lab6_grid.html')


if __name__ == '__main__':
    os.environ["FLASK_ENV"] = "dev"
    # Setting up database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Registering blueprints
    app.register_blueprint(home)
    app.register_blueprint(resources)
    app.register_blueprint(tree)
    app.register_blueprint(metro)

    # Adding API resources
    api.add_resource(ClientWrapper, '/api/clients/', '/api/clients/<int:client_id>')
    api.add_resource(OrderWrapper, '/api/orders/', '/api/orders/<int:client_id>', '/api/order/<int:order_id>')
    api.add_resource(LoginWrapper, '/api/login/')
    api.add_resource(LogoutWrapper, '/api/logout/')

    # RUNNING
    app.run(debug=True, host='127.0.0.1', port=5000)
