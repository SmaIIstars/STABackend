from flask import Flask


def routes(app):
    from . import login, personnel, emailCaptcha, register, filesUpload, filesDownload
    login.init_app(app)
    personnel.init_app(app)
    emailCaptcha.init_app(app)
    register.init_app(app)
    filesUpload.init_app(app)
    filesDownload.init_app(app)


def create_app():
    from . import db
    app = Flask(__name__)
    db.init_app(app)
    routes(app)
    return app


