"""App configuration."""
from os import environ, path
from dotenv import load_dotenv


# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# General Config
DEBUG = environ.get('DEBUG')

# MongoDB Config
MONGO_USERNAME = environ.get('MONGO_USERNAME')
MONGO_PASSWORD = environ.get('MONGO_PASSWORD')
MONGO_DB = environ.get('MONGO_DB')
MONGO_CLUSTER_URL = environ.get('MONGO_CLUSTER_URL')