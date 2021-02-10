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
import xlrd
from ..utils.skills import switch, get_root_path
import time


def routes(app):
    @app.route('/files/upload/<type_name>', methods=['POST'])
    def files_upload(type_name):
        file = request.files.get('file')
        root_path = get_root_path()

        def case_import():
            file_path = root_path + '/files/import/'
            file_name = str(int(time.time()))
            file_type = '.xlsx'
            # file.save(file_path + file_name + file_type)
            excel = xlrd.open_workbook(file_path + '1612841753983' + file_type)
            print(excel)

        def case_cover():
            path = root_path+'/files/cover'

        switcher = {
            'import': case_import,
            'cover': case_cover
        }
        switch(switcher, type_name)

        return {
            'message': 'successful',
            'status': '1000'
        }

