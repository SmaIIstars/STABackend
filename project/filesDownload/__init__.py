# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: __init__.py.py
# @time: 2021/2/3 23:29
from ..utils.skills import get_root_path
excel_template_path = get_root_path() + '/project/utils/excelTemplate'


def init_app(app):
    from . import download
    download.routes(app)



