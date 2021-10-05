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
    app.run(debug=True, host='127.0.0.1', port=5000)
