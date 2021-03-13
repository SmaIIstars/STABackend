# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/3/9 16:51
from flask_restful import Resource, fields, marshal
from flask import request
import json

from .models import User
from ..utils import custom_status_code
from ..db import db, file_type_switcher
from ..utils import authority

personnel_fields = {
    'email': fields.String(),
    'username': fields.String(attribute='username'),
    'authority': fields.String(attribute='uauthority'),
}


# user
class GetList(Resource):
    def get(self):
        data = User.query.filter(User.uauthority > authority['guest'] ).all()
        data = marshal(data, personnel_fields)
        return {
            'users': data,
            'message': 'user List'
        }


# Register
class Register(Resource):
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


# Login
class Login(Resource):
    user_fields = {
        'authority': fields.String(attribute='uauthority'),
        'username': fields.String(attribute='username')
    }

    def post(self):
        # raw | form-data
        data = json.loads(request.get_data(as_text=True))
        email = data['email']
        pwd = data['password']

        user_object = User.query.filter_by(email=email, upassword=pwd).first()
        if not user_object:
            return {
                'code': 1001,
                'message': custom_status_code[1001]
            }

        data = marshal(user_object, Login.user_fields)
        from ..utils.authority import create_token
        token = create_token({'data': data}, 60*24*7)
        data['token'] = token
        return {
            'code': 1000,
            'data': data,
            'message': custom_status_code[1000]
        }


# Authority
class ChageAuthority(Resource):
    def post(self):
        data = json.loads(request.get_data(as_text=True))
        email = data['email']
        authority = data['authority']
        # db.session.query(User).filter_by(email=email).update({file_type_switcher['authority']: authority})

        print(file_type_switcher['user'])



        return {
            "data": 1000
        }



