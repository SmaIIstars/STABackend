# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/1/24 17:22
from flask_restful import Resource, fields
from flask import request
from ..user.models import User
from ..db import db
from ..utils import authority


class RegisterView(Resource):
    def post(self):
        data = request.json
        [username, password, email] = data
        user = User(username, password, email, authority['guest'])
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as err:
            return {
                'code': 1004,
                'message': '该邮箱已经注册!'
            }

        return {
            'message': 'successful'
        }





