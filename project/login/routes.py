# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site:
# @software: PyCharm
# @file: routes.py
# @time: 2020/12/21 17:01
from .views import *
from flask_restful import Api
from . import login_bp


def add_resources(api):
    api.add_resource(Login, '/login')


def register_blueprints(app):
    app.register_blueprint(login_bp, url_prefix='')


def init_app(app):
    api = Api(login_bp)
    register_blueprints(app)
    add_resources(api)







