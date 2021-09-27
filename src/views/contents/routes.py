from .home import home
from .metro import metro
from .register import register
from .resources import resources
from .tree import tree


def initialise_contents(app):
	app.register_blueprint(home)
	app.register_blueprint(register)
	app.register_blueprint(resources)
	app.register_blueprint(tree)
	app.register_blueprint(metro)
