# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/1/13 15:53
from flask_restful import Resource, fields, marshal
from .models import Personnel
from flask import request
import json
from ..utils import custom_status_code
from ..db import db, file_type_switcher


personnel_fields = {
    'id': fields.String(attribute='perid'),
    'name': fields.String(attribute='pername'),
    'degree': fields.String(attribute='perdegree'),
    'EB': fields.String(attribute='pereb'),
    'title': fields.String(attribute='pertitle'),
}


class GetList(Resource):
    def post(self):
        # get request params
        # print(request.args.get('token'))
        # Obtain token and determine the validity
        from ..utils.authority import valid_token
        res_valid_token = valid_token(request)
        if res_valid_token['code'] == 1003:
            return res_valid_token

        data = Personnel.query.all()
        data = marshal(data, personnel_fields)
        return {
            'data': data,
            'message': 'personnel'
        }


class Update(Resource):
    def post(self):
        data = json.loads(request.get_data())

        try:
            user, info = data['user'], data['info']
            key = info['id']
            del info['id']
            item_keys = file_type_switcher['personnel'][1:]
            info = dict(zip(item_keys, info.values()))
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(Personnel).filter_by(perid=key).update(info)
            db.session.commit()

        except BaseException as e:
            return {
                'code': 1201,
                'message': '{}: {}'.format(custom_status_code[1201], str(e)),
            }

        return {
            'code': 1200,
            'message': 'Update: {}'.format(custom_status_code[1200]),
        }


class Delete(Resource):
    def post(self):
        data = json.loads(request.get_data())

        try:
            user, info = data['user'], data['info']
            key = info['id']
            del info['id']
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(Personnel).filter_by(perid=key).delete()
            db.session.commit()

        except BaseException as e:
            return {
                'code': 1201,
                'message': '{}: {}'.format(custom_status_code[1201], str(e)),
            }

        return {
            'code': 1200,
            'message': 'Delete: {}'.format(custom_status_code[1200])
        }



