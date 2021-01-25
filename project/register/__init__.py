# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: __init__.py.py
# @time: 2021/1/24 17:21

from flask import Blueprint
register_bp = Blueprint('register', __name__)


def init_app(app):
    from . import routes
    routes.init_app(app)
