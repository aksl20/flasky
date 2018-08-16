from dotenv import load_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fuck'
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@db_test:5432/{}".format(os.environ.get('DB'),
                                                     os.environ.get('DB_USER_TEST'),
                                                     os.environ.get('DB_PASSWORD_TEST'),
                                                     os.environ.get('NAME_TEST'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

