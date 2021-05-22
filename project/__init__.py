from flask import Flask


def routes(app):
    from . import emailCaptcha, files, user, personnel, \
        project, paper, patent, monograph, srta, meeting
    emailCaptcha.init_app(app)
    files.init_app(app)
    user.init_app(app)

    personnel.init_app(app)
    project.init_app(app)
    paper.init_app(app)
    patent.init_app(app)
    monograph.init_app(app)
    srta.init_app(app)
    meeting.init_app(app)


def create_app():
    from . import db
    app = Flask(__name__)
    db.init_app(app)
    routes(app)
    print(app.url_map)
    return app


