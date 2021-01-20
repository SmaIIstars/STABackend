from flask import Blueprint
user_bp = Blueprint('user', __name__)


def init_app(app):
    from . import routes
    routes.init_app(app)
    # print(app.url_map)



