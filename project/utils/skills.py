# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: skills.py
# @time: 2021/1/25 16:08
def format_print(name, main_body):
    print('{}: {}'.format(name, main_body))
    return main_body


def get_root_path():
    import project
    return path_format(get_current_path(project.__name__))


def get_current_path(file_name):
    from os import path
    return path_format(path.abspath(path.dirname(file_name)))


def path_format(path):
    return path.replace('\\', '/')
