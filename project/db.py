# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: db.py
# @time: 2020/12/21 16:59
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    global db
    db = SQLAlchemy(app)







