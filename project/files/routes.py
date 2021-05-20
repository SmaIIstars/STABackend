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
import time
import xlrd

from ..utils.skills import switch
from ..db import file_type_switcher, db
from ..utils import custom_status_code
from .constant import EXCEL_TEMPLATE_PATH, ITEMS_LEN_LIST, ROOT_PATH
from ..personnel.models import Personnel
from ..project.models import Project


def download(app):
    @app.route('/files/download', methods=['get'])
    def files_download():
        filename = request.args.get('fileName')

        try:
            return send_from_directory(EXCEL_TEMPLATE_PATH, filename+'.xlsx')
        except Exception as e:
            return {
                'code': 1101,
                'message': '{}: {}'.format(custom_status_code[1101], str(e))
            }


generate_object_switcher = {
    # The reason of form refer to source code of switch
    'personnel': lambda: lambda keys, values: Personnel(**dict(zip(keys, values))),
    'project': lambda: lambda keys, values: Project(**dict(zip(keys, values))),
}


def upload(app):
    @app.route('/files/upload/<type_name>', methods=['POST'])
    def files_upload(type_name):
        file = request.files.get('file')
        table_name = request.args['type']

        def case_import():
            insert_items(file, type_name, table_name)

        def case_cover():
            delete_all_items(table_name)
            insert_items(file, type_name, table_name)

        upload_type_switcher = {
            'import': case_import,
            'cover': case_cover
        }
        switch(upload_type_switcher, type_name)

        return {
            'code': 1100,
            'message': custom_status_code[1100]
        }


def insert_items(file, type_name, table_name):
    table_items = file_type_switcher[table_name]
    file_path = ROOT_PATH + '/files/{}/'.format(type_name)
    file_name = str(int(time.time()))
    file_type = '.xlsx'
    file.save(file_path + file_name + file_type)

    workbook = xlrd.open_workbook(file_path + file_name + file_type)
    sheet = workbook.sheet_by_index(0)
    rows, cols = sheet.nrows, sheet.ncols
    # sql = tsql['insert'].format('sta', ', '.join(table_items), '')

    # values = ''
    items_list = []

    print('table_items: {}, '.format(table_items))

    for i in range(1, rows):
        # [table_items] = sheet.row_values(i)
        item = switch(generate_object_switcher, table_name)(table_items, sheet.row_values(i))
        items_list.append(item)
        # format of multiple values
        # values += '({}), '.format(', '.join(sheet.row_values(i)))
        if i % ITEMS_LEN_LIST == 0:
            # delete the last comma
            # add(sql.format(values)[:-2])
            db.session().add_all(items_list)
            items_list.clear()
            # values = ''
            # sql = tsql['insert'].format('sta', ', '.join(table_items), '')
    db.session().add_all(items_list)
    try:
        db.session().commit()
    except BaseException as e:
        return {
            'code': 1101,
            'message': '{}: {}'.format(custom_status_code[1101], str(e))
        }


def delete_all_items(class_name):
    class_type_switcher = {
        'personnel': Personnel,
        'project': Project
    }

    items_list = switch(class_type_switcher, class_name).query.all()
    index = 0

    for item in items_list:
        index += 1
        db.session.delete(item)
        if index >= ITEMS_LEN_LIST:
            db.session().commit()
            index = 0

    db.session().commit()


