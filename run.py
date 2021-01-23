import seetings
from project import create_app


if __name__ == '__main__':
    app = create_app()
    app.config.from_object(seetings.DevelopmentConfig)
    app.run()





