# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: views.py
# @time: 2021/4/27 15:52
from flask_restful import Resource, fields, marshal
from .models import Project
from flask import request
import json
from ..utils import custom_status_code
from ..db import db, file_type_switcher

'''
proid: "项目编号",
name: "项目名称",
year: "年度",
category: "类别",
header: "项目负责人",
member: "项目成员",
st: "开始时间",
et: "结束时间",
uu: "承担单位",
pf: "项目经费",
gu: "拨款单位",
'''

project_fields = {
    'id': fields.String(attribute='proid'),
    'name': fields.String(attribute='proname'),
    'year': fields.String(attribute='proyear'),
    'category': fields.String(attribute='procategory'),
    'header': fields.String(attribute='proheader'),
    'member': fields.String(attribute='promember'),
    'st': fields.String(attribute='prost'),
    'et': fields.String(attribute='proet'),
    'uu': fields.String(attribute='prouu'),
    'pf': fields.String(attribute='propf'),
    'gu': fields.String(attribute='progu'),
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
        total = Project.query.count()

        if qtype == 'all':
            data = Project.query.all()
            data = marshal(data, project_fields)
            return {
                'data': data,
                'total': total,
                'message': 'project List'
            }
        else:
            current_page, page_size = int(params['currentPage']), int(params['pageSize'])

            data = Project.query.paginate(page=current_page, per_page=page_size).items
            data = marshal(data, project_fields)
            return {
                'data': data,
                'total': total,
                'message': 'project List'
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
            item_keys = file_type_switcher['project'][1:]
            info = dict(zip(item_keys, info.values()))
            # print(info)
            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            db.session.query(Project).filter_by(proid=key).update(info)
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

            db.session.query(Project).filter_by(proid=key).delete()
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
            id, name, year, category, header, member, st, et, uu, pf, gu = info.values()

            from ..utils.authority import valid_authority
            res_valid_authority = valid_authority(user['authority'], 'admin')
            if res_valid_authority['code'] == 1201:
                return res_valid_authority

            project = Project(id, name, year, category, header, member, st, et, uu, pf, gu)
            db.session.add(project)
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

