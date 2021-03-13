# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: __init__.py.py
# @time: 2021/3/9 16:41
from flask import Blueprint
user_bp = Blueprint('user', __name__)
register_bp = Blueprint('register', __name__)
login_bp = Blueprint('login', __name__)
authority_bp = Blueprint('authority', __name__)


def init_app(app):
    from . import routes
    routes.init_app(app)
