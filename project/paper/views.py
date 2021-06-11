# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/5/21 8:16

from flask_restful import Resource, fields, marshal
from .models import Paper
from flask import request
import json
from ..utils import custom_status_code
from ..db import db, file_type_switcher


paper_fields = {
    'id': fields.String(attribute='paperid'),
    'name': fields.String(attribute='papername'),
    'fa': fields.String(attribute='paperfa'),
    'ca': fields.String(attribute='paperca'),
    'pt': fields.String(attribute='paperpt'),
    'pn': fields.String(attribute='paperpn'),
    'vp': fields.String(attribute='papervp'),
    'sp': fields.String(attribute='papersp'),
    'ep': fields.String(attribute='paperep'),
    'ct': fields.String(attribute='paperct'),
}


class GetList(Resource):
    def get(self):
        from ..utils.authority import valid_token
        res_valid_token = valid_token(request)
        if res_valid_token['code'] == 1003:
            return res_valid_token

        params = request.args
        # print(params)
        qtype = params['type']
        total = Paper.query.count()

        if qtype == 'all':
            data = Paper.query.all()
            data = marshal(data, paper_fields)
            print('data:', data)
            return {
                'data': data,
                'total': total,
                'message': 'paper List'
            }
        else:
            current_page, page_size = int(params['currentPage']), int(params['pageSize'])

            data = Paper.query.paginate(page=current_page, per_page=page_size).items
            data = marshal(data, paper_fields)
            return {
                'data': data,
                'total': total,
                'message': 'paper List'
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
            item_keys = file_type_switcher['paper'][1:]
            info = dict(zip(item_keys, info.values()))
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(Paper).filter_by(paperid=key).update(info)
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

            db.session.query(Paper).filter_by(paperid=key).delete()
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
            proid, name, year, category, header, member, st, et, uu, pf, gu = info.values()

            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            paper = Paper(proid, name, year, category, header, member, st, et, uu, pf, gu)
            db.session.add(paper)
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

