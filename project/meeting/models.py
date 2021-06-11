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


class Meeting(db.Model):
    mid = db.Column(db.String(255), primary_key=True)
    mname = db.Column(db.String(255))
    mmember = db.Column(db.String(255))
    mtime = db.Column(db.String(255))
    maddress = db.Column(db.String(255))
    mtype = db.Column(db.String(255))
    mnote = db.Column(db.String(255))

    def __init__(self, mid, mname, mmember, mtime, maddress, mtype, mnote):
        self.mid = mid
        self.mname = mname
        self.mmember = mmember
        self.mtime = mtime
        self.maddress = maddress
        self.mtype = mtype
        self.mnote = mnote




