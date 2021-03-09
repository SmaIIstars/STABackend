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
from ..db import file_type_switcher, db
import time
from ..personnel.models import Personnel
from ..utils import custom_status_code


ITEMS_LEN_LIST = 5
generate_object_switcher = {
    # The reason of form refer to source code of switch
    'personnel': lambda: lambda keys, values: Personnel(**dict(zip(keys, values))),
    '': ''
}
root_path = get_root_path()


def routes(app):
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
    file_path = root_path + '/files/{}/'.format(type_name)
    file_name = str(int(time.time()))
    file_type = '.xlsx'
    file.save(file_path + file_name + file_type)
    workbook = xlrd.open_workbook(file_path + file_name + file_type)
    sheet = workbook.sheet_by_index(0)
    rows, cols = sheet.nrows, sheet.ncols
    # sql = tsql['insert'].format('sta', ', '.join(table_items), '')

    # values = ''
    items_list = []

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
        'personnel': Personnel
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
