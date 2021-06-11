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
from .models import SRTA
from flask import request
import json
from ..utils import custom_status_code
from ..db import db, file_type_switcher


srta_fields = {
    'id': fields.String(attribute='staid'),
    'name': fields.String(attribute='staname'),
    'type': fields.String(attribute='statype'),
    'winner': fields.String(attribute='stawinner'),
    'rt': fields.String(attribute='start'),
    'time': fields.String(attribute='statime'),
    'it': fields.String(attribute='stait'),
    'note': fields.String(attribute='stanote'),
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
        total = SRTA.query.count()

        if qtype == 'all':
            data = SRTA.query.all()
            data = marshal(data, srta_fields)
            return {
                'data': data,
                'total': total,
                'message': 'srta List'
            }
        else:
            current_page, page_size = int(params['currentPage']), int(params['pageSize'])

            data = SRTA.query.paginate(page=current_page, per_page=page_size).items
            data = marshal(data, srta_fields)
            return {
                'data': data,
                'total': total,
                'message': 'srta List'
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
            item_keys = file_type_switcher['srta'][1:]
            info = dict(zip(item_keys, info.values()))
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(SRTA).filter_by(staid=key).update(info)
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

            db.session.query(SRTA).filter_by(staid=key).delete()
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
            id, name, type, winner, rt, time, it, note = info.values()
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            srta = SRTA(id, name, type, winner, rt, time, it, note)
            db.session.add(srta)
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
