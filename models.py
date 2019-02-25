
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_URL = 'https://tinyurl.com/truffle-cupcake'


def connect_db(app):
        """ connect to db"""
        db.app = app
        db.init_app(app)


class Cupcakes(db.Model):
    ''' SQLALChemy Cupcakes class'''
    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)

    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)

    rating = db.Column(db.Float,
                       nullable=False)

    image = db.Column(db.Text, default=DEFAULT_URL)
