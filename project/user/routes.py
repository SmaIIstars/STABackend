# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: routes.py
# @time: 2021/3/9 16:50
from .views import *
from flask_restful import Api
from . import user_bp, register_bp, login_bp, authority_bp

bp_list = [user_bp, register_bp, login_bp, authority_bp]
bp_order = {
    'user': 0,
    'register': 1,
    'login': 2,
    'authority': 3
}


def add_resources(apis):
    apis[bp_order['user']].add_resource(GetList, '/getlist')
    apis[bp_order['register']].add_resource(Register, '/register')
    apis[bp_order['login']].add_resource(Login, '/login')
    apis[bp_order['authority']].add_resource(ChageAuthority, '/change')


def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(register_bp, url_prefix='')
    app.register_blueprint(login_bp, url_prefix='')
    app.register_blueprint(authority_bp, url_prefix='/authority')


def init_app(app):
    api_list = list(map(lambda bp: Api(bp), bp_list))
    register_blueprints(app)
    add_resources(api_list)
