# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: models.py
# @time: 2021/5/21 8:16
from project.db import db


class Paper(db.Model):
    paperid = db.Column(db.String(255), primary_key=True)
    papername = db.Column(db.String(255))
    paperfa = db.Column(db.String(255))
    paperca = db.Column(db.String(255))
    paperpt = db.Column(db.String(255))
    paperpn = db.Column(db.String(255))
    papervp = db.Column(db.String(255))
    papersp = db.Column(db.String(255))
    paperep = db.Column(db.String(255))
    paperct = db.Column(db.String(255))

    def __init__(self, paperid, papername, paperfa, paperca, paperpt, paperpn,
                 papervp, papersp, paperep, paperct):
        self.paperid = paperid
        self.papername = papername
        self.paperfa = paperfa
        self.paperca = paperca
        self.paperpt = paperpt
        self.paperpn = paperpn
        self.papervp = papervp
        self.papersp = papersp
        self.paperep = paperep
        self.paperct = paperct



