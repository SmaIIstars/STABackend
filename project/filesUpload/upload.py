# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: files.py
# @time: 2021/1/30 19:48
from flask import request


def routes(app):
    @app.route('/files/upload', methods=['POST'])
    def files_upload():
        print(request.files)
        print(request.form)
        # print(request.headers)
        return {
            'message': 'successful',
            'status': '1000'
        }

