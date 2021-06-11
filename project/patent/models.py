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


class Patent(db.Model):
    paid = db.Column(db.String(255), primary_key=True)
    paname = db.Column(db.String(255))
    paapplicant = db.Column(db.String(255))
    pada = db.Column(db.String(255))
    patype = db.Column(db.String(255))
    paie = db.Column(db.String(255))
    paapc = db.Column(db.String(255))
    paauc = db.Column(db.String(255))

    def __init__(self, paid, paname, paapplicant, pada, patype, paie, paapc, paauc):
        self.paid = paid
        self.paname = paname
        self.paapplicant = paapplicant
        self.pada = pada
        self.patype = patype
        self.paie = paie
        self.paapc = paapc
        self.paauc = paauc




