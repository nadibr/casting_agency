import os
from dotenv import load_dotenv
from sqlalchemy import Column, String, Integer, DateTime, VARCHAR, create_engine
from flask_sqlalchemy import SQLAlchemy

# DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
# DB_USER = os.getenv('DB_USER', 'postgres')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
# DB_NAME = os.getenv('DB_NAME', 'castagency')

# DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
load_dotenv()
# DB_PATH = 'postgresql://postgres:password@localhost:5432/castingagency'

# DATABASE_URL = 'postgres://rvcvvxcwiexiuv:87016bf027cf5e87f25e4d3b2ba6e6e42c34b00cd443947547ae0365e11f5eae@ec2-3-211-167-220.compute-1.amazonaws.com:5432/d6250asughmup8'
DATABASE_URL = os.getenv('DATABASE_URL')

db = SQLAlchemy()


def setup_db(app, database_path=DATABASE_URL):
    app.config.from_object('config')
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
#    db.create_all()


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(DateTime)
    gender = Column(VARCHAR(1))

    def __init__(self, name, birth_date, gender):
        self.name = name,
        self.birth_date = birth_date,
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date,
            'gender': self.gender
        }


class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)