import os
from redis import Redis

class Config:
    BASE_URL: str = "http://89.223.71.158:9090/"
    STATICS_FILEPATH: str = 'static'
    STATICS_URLPATH: str = '/static'

    SECRET_KEY = os.environ.get('SECRET_KEY') or b'blablabla'
    WTF_CSRF_SECRET_KEY = 'a random string'
    RECAPTCHA_PUBLIC_KEY = 'test'

    PATH_TO_DIR = os.path.dirname(os.path.abspath(__file__))

    # avatar
    AVATAR_DIR = '/uploads/us_avatars/'
    FULL_AVATAR_DIR = os.path.join(PATH_TO_DIR, 'static/'+AVATAR_DIR)

     # Database
    db_name = os.environ.get('DB_NAME', 'dnddbase')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'postgres')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    def database_link():
        return f'postgresql://{Config.db_user}:{Config.db_password}@'\
               f'{Config.db_host}:{Config.db_port}/{Config.db_name}'

    # Redis
    REDIS_URL = 'redis://localhost:6379/0'
    redis = Redis()

    #GMail
    GMAIL_LOGIN = "dmnddproject@gmail.com"
    GMAIL_PASSWORD = "rblehhtujcupnruf"

    # User role
    role: dict = {
        'admin': 900,
        'author': 800,
        'moderator': 700,
        'user_verified': 101,
        'user': 100
    }


config = Config()
