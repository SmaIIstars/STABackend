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
import json
from flask import request
from ..utils.skills import format_print


class RegisterView(Resource):
    def post(self):
        # data = json.loads(request.get_data(as_text=True))
        data1 = format_print('get_data', request.get_data(as_text=True))
        data2 = format_print('json', request.json)
        print(type(data1))
        print(type(data2))
        return {
            'message': 'successful'
        }





