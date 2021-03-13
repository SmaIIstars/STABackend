# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2021/3/9 16:41
from project.db import db


class User(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255))
    upassword = db.Column(db.String(255))
    uauthority = db.Column(db.Integer)

    def __init__(self, username, password, email, authority):
        self.email = email
        self.username = username
        self.upassword = password
        self.uauthority = authority

