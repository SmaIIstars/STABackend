# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: download.py
# @time: 2021/2/3 23:29
from flask import request, send_from_directory


def routes(app):
    @app.route('/files/download', methods=['get'])
    def files_download():
        filename = request.args.get('fileName')

        try:
            return send_from_directory('E:/Code/Python/STABackend/project/utils/excelTemplate', filename)

        except Exception as e:
            return {
                'message': str(e),
                'status': '1001'
            }
        # return {
        #     'message': 'successful',
        #     'status': '1001'
        # }




