# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/5/21 11:42
from flask_restful import Resource, fields, marshal
from .models import Monograph
from flask import request
import json
from ..utils import custom_status_code
from ..db import db, file_type_switcher


monograph_fields = {
    'id': fields.String(attribute='moissn'),
    'name': fields.String(attribute='moname'),
    'author': fields.String(attribute='moauthor'),
    'press': fields.String(attribute='mopress'),
    'dp': fields.String(attribute='modp'),
}


class GetList(Resource):
    def get(self):
        # get request params
        # print('token:', request.args)
        # Obtain token and determine the validity

        from ..utils.authority import valid_token
        res_valid_token = valid_token(request)
        if res_valid_token['code'] == 1003:
            return res_valid_token

        params = request.args
        # print(params)
        qtype = params['type']
        total = Monograph.query.count()

        if qtype == 'all':
            data = Monograph.query.all()
            data = marshal(data, monograph_fields)
            return {
                'data': data,
                'total': total,
                'message': 'monograph List'
            }
        else:
            current_page, page_size = int(params['currentPage']), int(params['pageSize'])

            data = Monograph.query.paginate(page=current_page, per_page=page_size).items
            data = marshal(data, monograph_fields)
            return {
                'data': data,
                'total': total,
                'message': 'monograph List'
            }


class Update(Resource):
    def post(self):
        data = json.loads(request.get_data())

        try:
            user, info = data['user'], data['info']

            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            key = info['id']
            del info['id']
            item_keys = file_type_switcher['monograph'][1:]
            info = dict(zip(item_keys, info.values()))
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(Monograph).filter_by(moissn=key).update(info)
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

            db.session.query(Monograph).filter_by(moissn=key).delete()
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


class Add(Resource):
    def post(self):
        data = json.loads(request.get_data())

        try:
            user, info = data['user'], data['info']
            id, name, author, press, dp = info.values()
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            monograph = Monograph(id, name, author, press, dp)
            db.session.add(monograph)
            db.session.commit()

        except BaseException as e:
            return {
                'code': 1201,
                'message': '{}: {}'.format(custom_status_code[1201], str(e)),
            }

        return {
            'code': 1200,
            'message': 'Add: {}'.format(custom_status_code[1200])
        }
