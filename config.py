import os
# SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@localhost:5432/CA'
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False