# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: routes.py
# @time: 2021/5/21 11:42
from .views import *
from flask_restful import Api
from . import meeting_bp


def add_resources(api):
    api.add_resource(GetList, '/getlist')
    api.add_resource(Update, '/change')
    api.add_resource(Delete, '/delete')
    api.add_resource(Add, '/add')


def register_blueprints(app):
    app.register_blueprint(meeting_bp, url_prefix='/meeting')


def init_app(app):
    api = Api(meeting_bp)
    register_blueprints(app)
    add_resources(api)
