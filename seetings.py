class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(BaseConfig):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '808069'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'cms'
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'sta'
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True



