# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: download.py
# @time: 2021/2/3 23:29
from flask import request


def routes(app):
    @app.route('/files/download', methods=['get'])
    def files_download():
        print(request.args)

        return {
            'message': 'successful',
            'status': '1000'
        }