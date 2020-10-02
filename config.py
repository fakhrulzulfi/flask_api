import os 

# basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    HOST = str(os.environ.get('DB_HOST'))
    USERNAME = str(os.environ.get('DB_USER'))
    PASSWORD = str(os.environ.get('DB_PASS'))
    DATABASE = str(os.environ.get('DB_NAME'))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ USERNAME +':'+ PASSWORD +'@'+ HOST +'/'+ DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_RECORD_QUERIES=True

    ## config for image uploads ##
    UPLOAD_FOLDER = './uploads/'
    MAX_CONTENT_LENGTH = 1024*1024
    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png']

    JWT_SECRET_KEY = str(os.environ.get('JWT_SECRET'))