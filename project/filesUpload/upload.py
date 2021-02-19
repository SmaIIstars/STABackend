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
from ..db import tsql, file_type_switcher, add
import time

ITEMS_LEN_LIST = 5
items_list = []


def routes(app):
    @app.route('/files/upload/<type_name>', methods=['POST'])
    def files_upload(type_name):
        file = request.files.get('file')
        root_path = get_root_path()
        table_name = 'personnel'
        table_items = file_type_switcher[table_name]

        def case_import():
            file_path = root_path + '/files/import/'
            file_name = str(int(time.time()))
            file_type = '.xlsx'
            # file.save(file_path + file_name + file_type)
            workbook = xlrd.open_workbook(file_path + '1612841753983' + file_type)
            sheet = workbook.sheet_by_index(0)
            rows, cols = sheet.nrows, sheet.ncols
            sql = tsql['insert'].format('sta', ', '.join(table_items), '')

            values = ''
            for i in range(1, rows):
                items_list.append(sheet.row_values(i))
                # format of multiple values
                values += '({}), '.format(', '.join(sheet.row_values(i)))
                if i % ITEMS_LEN_LIST == 0:
                    # delete the last comma
                    add(sql.format(values)[:-2])
                    items_list.clear()
                    values = ''
                    sql = tsql['insert'].format('sta', ', '.join(table_items), '')
            print(sql.format(values)[:-2])

        def case_cover():
            path = root_path+'/files/cover'

        upload_type_switcher = {
            'import': case_import,
            'cover': case_cover
        }
        switch(upload_type_switcher, type_name)

        return {
            'message': 'successful',
            'status': '1000'
        }

