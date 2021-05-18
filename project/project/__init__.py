# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: __init__.py.py
# @time: 2021/4/27 15:52
from flask import Blueprint
project_bp = Blueprint('project', __name__)


def init_app(app):
    from . import routes
    routes.init_app(app)

