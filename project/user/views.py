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
from ..db import db
from ..utils import authority, custom_status_code

user_fields = {
    'email': fields.String(),
    'username': fields.String(attribute='username'),
    'authority': fields.String(attribute='uauthority'),
}

user_items = {
    'email': User.email,
    'username': User.username,
    'authority': User.uauthority,
}


# user
class GetList(Resource):
    def get(self):
        data = User.query.filter(User.uauthority > authority['guest']).all()
        data = marshal(data, user_fields)
        return {
            'users': data,
            'message': 'get User List'
        }


class GetUser(Resource):
    def get(self):
        args = request.args.to_dict()
        keys, values = list(args.keys()), list(args.values())

        # default value
        users = []
        if len(values) > 0 and values[0] != "":
            users = User.query.filter(user_items[keys[0]].contains(values[0])).all()

        # Here is a multi-condition query, not tested. It's a medium serious problem
        # if len(keys) > 1:
        #     for key in keys[1:]:
        #         pass

        users = marshal(users, user_fields)
        return {
            'users': users,
            'message': 'get User'
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
        try:
            user, info = data['user'], data['info']

            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            if isinstance(info, dict):
                email, authority = info['email'], info['authority']
                db.session.query(User).filter_by(email=email).update({'uauthority': authority})
                # print(file_type_switcher['user'][file_type_switcher['user'].index('uauthority')])
                db.session.commit()
            elif isinstance(info, list):
                print(info)
                for item in info:
                    email, authority = item['email'], item['authority']
                    db.session.query(User).filter_by(email=email).update({'uauthority': authority})
                db.session.commit()
            return {
                "code": 1300,
                "message": custom_status_code[1300]
            }
        except BaseException as e:
            return {
                'code': 1301,
                'message': '{}: {}'.format(custom_status_code[1301], str(e)),
            }





