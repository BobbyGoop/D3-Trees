from main import app
from flask_sqlalchemy import SQLAlchemy

# engine = create_engine('sqlite:///store.db')
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
#
# Base = declarative_base()
# Base.query = db_session.query_property()


db = SQLAlchemy(app)

