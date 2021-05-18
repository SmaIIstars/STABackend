# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2021/4/27 15:52
from project.db import db


class Project(db.Model):
    proid = db.Column(db.String(255), primary_key=True)
    proname = db.Column(db.String(255))
    proyear = db.Column(db.String(255))
    procategory = db.Column(db.String(255))
    proheader = db.Column(db.String(255))
    promember = db.Column(db.String(255))
    prost = db.Column(db.String(255))
    proet = db.Column(db.String(255))
    prouu = db.Column(db.String(255))
    propf = db.Column(db.String(255))
    progu = db.Column(db.String(255))

    def __init__(self, perid, pername, perdegree, pereb, pertitle):
        self.perid = perid
        self.pername = pername
        self.perdegree = perdegree
        self.pereb = pereb
        self.pertitle = pertitle


