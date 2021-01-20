# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2020/12/21 18:49
from project.db import db


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(255), primary_key=True)
    upassword = db.Column(db.String(255))
    uauthority = db.Column(db.Integer)






