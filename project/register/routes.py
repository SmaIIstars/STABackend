# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: routes.py
# @time: 2021/1/24 17:22
from .views import *
from flask_restful import Api
from . import register_bp


def register_blueprints(app):
    app.register_blueprint(register_bp, url_prefix='')


def add_resources(api):
    api.add_resource(RegisterView, '/register')


def init_app(app):
    api = Api(register_bp)
    register_blueprints(app)
    add_resources(api)
