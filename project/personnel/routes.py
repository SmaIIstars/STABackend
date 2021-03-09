# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: routes.py
# @time: 2021/1/13 15:53

from .views import *
from flask_restful import Api
from . import personnel_bp


def add_resources(api):
    api.add_resource(GetList, '/getlist')
    api.add_resource(Update, '/change')
    api.add_resource(Delete, '/delete')


def register_blueprints(app):
    app.register_blueprint(personnel_bp, url_prefix='/personnel')


def init_app(app):
    api = Api(personnel_bp)
    register_blueprints(app)
    add_resources(api)

