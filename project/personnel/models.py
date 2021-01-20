# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2021/1/13 15:53
from project.db import db


class Personnel(db.Model):
    perid = db.Column(db.String(255), primary_key=True)
    pername = db.Column(db.String(255))
    perdegree = db.Column(db.String(255))
    pereb = db.Column(db.String(255))
    pertitle = db.Column(db.String(255))


