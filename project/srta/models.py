# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2021/5/21 11:42
from project.db import db


class SRTA(db.Model):
    staid = db.Column(db.String(255), primary_key=True)
    staname = db.Column(db.String(255))
    statype = db.Column(db.String(255))
    stawinner = db.Column(db.String(255))
    start = db.Column(db.String(255))
    statime = db.Column(db.String(255))
    stait = db.Column(db.String(255))
    stanote = db.Column(db.String(255))

    def __init__(self, staid, staname, statype, stawinner, start,
                 statime, stait, stanote):
        self.staid = staid
        self.staname = staname
        self.statype = statype
        self.stawinner = stawinner
        self.start = start
        self.statime = statime
        self.stait = stait
        self.stanote = stanote




