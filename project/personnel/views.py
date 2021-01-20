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


class PersonnelView(Resource):
    personnel_fields = {
        'id': fields.String(attribute='perid'),
        'name': fields.String(attribute='pername'),
        'degree': fields.String(attribute='perdegree'),
        'EB': fields.String(attribute='pereb'),
        'title': fields.String(attribute='pertitle'),
    }

    def post(self):
        # get request params
        # print(request.args.get('token'))
        # Obtain token and determine the validity
        from ..utils.token import valid_token
        res_valid_token = valid_token(request)
        if res_valid_token['code'] == 1003:
            return res_valid_token

        data = Personnel.query.all()
        data = marshal(data, PersonnelView.personnel_fields)
        return {
            'data': data,
            'message': 'personnel'
        }



