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

# A special format for assigning values twice.
# tsql = {
#     'insert': 'INSERT INTO {} ({}) VALUES {{}}'
# }

file_type_switcher = {
    'user': ['email', 'username'] + list(map(lambda item: 'u'+item, ['password', 'authority'])),

    'personnel': list(map(lambda item: 'per'+item, ['id', 'name', 'degree',
                                                    'eb', 'title'])),

    'project': list(map(lambda item: 'pro' + item, ['id', 'name', 'year',
                                                    'category', 'header',
                                                    'member', 'st', 'et', 'uu'])),

    'paper': list(map(lambda item: 'paper'+item, ['id', 'name', 'fa',
                                                  'ca', 'pt', 'pn', 'vp',
                                                  'sp', 'ep', 'ct'])),

    'patent': list(map(lambda item: 'pa' + item, ['id', 'name', 'applicant',
                                                  'da', 'type', 'ie',
                                                  'apc', 'auc'])),

    'monograph': list(map(lambda item: 'mo' + item, ['isbn', 'name', 'author',
                                                     'press.', 'dp'])),

    'srta': list(map(lambda item: 'sta' + item, ['id', 'name', 'type',
                                                'winner', 'rt', 'time',
                                                'it', 'note'])),

    'meeting': list(map(lambda item: 'm' + item, ['id', 'name', 'member',
                                                   'time', 'address', 'type',
                                                   'note'])),
}


def init_app(app):
    global db
    db = SQLAlchemy(app)









