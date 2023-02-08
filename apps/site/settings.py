import os

class Config:
    STATICS_FILEPATH: str = 'apps/site/static'
    STATICS_URLPATH: str = '/static'

    SECRET_KEY = os.environ.get('SECRET_KEY') or b'blablabla'
    WTF_CSRF_SECRET_KEY = 'a random string'
    RECAPTCHA_PUBLIC_KEY = 'test'

    PATH_TO_DIR = os.path.dirname(os.path.abspath(__file__))

     # Database
    db_name = os.environ.get('DB_NAME', 'dnddbase')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'postgres')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    def database_link():
        return f'postgresql://{Config.db_user}:{Config.db_password}@'\
               f'{Config.db_host}:{Config.db_port}/{Config.db_name}'


config = Config()
