# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: __init__.py.py
# @time: 2021/1/20 16:34
custom_status_code = {
    # login & register & captcha
    1000: 'Login successful',
    1001: 'Email or password error',

    1002: 'Valid token successful',
    1003: 'Valid token failed',

    1004: 'Email is registered',

    # files
    1100: '',
    1101: 'files upload error',

    # authority
    1200: 'Access',
    1201: 'Access denied',

    # operation
    1300: 'Operation is successful',
    1301: 'Operation is failed'
}

from_email = {
    "user": 'smallstars.he@qq.com',
    "password": 'cjfoeqsqkylbbfgi',
    "host": 'smtp.qq.com'
}

authority = {
    'guest': 0,
    'admin': 1,
    'superAdmin': 2
}
