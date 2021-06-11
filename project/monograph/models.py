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


class Monograph(db.Model):
    moissn = db.Column(db.String(255), primary_key=True)
    moname = db.Column(db.String(255))
    moauthor = db.Column(db.String(255))
    mopress = db.Column(db.String(255))
    modp = db.Column(db.String(255))

    def __init__(self, moissn, moname, moauthor, mopress, modp):
        self.moissn = moissn
        self.moname = moname
        self.moauthor = moauthor
        self.mopress = mopress
        self.modp = modp




