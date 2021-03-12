from flask import Flask


def routes(app):
    from . import personnel, emailCaptcha, files, user
    personnel.init_app(app)
    emailCaptcha.init_app(app)
    files.init_app(app)
    user.init_app(app)


def create_app():
    from . import db
    app = Flask(__name__)
    db.init_app(app)
    routes(app)
    print(app.url_map)
    return app


