# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: token.py
# @time: 2021/1/20 14:15
from . import *
# JWT
salt = 'smallstars'


def create_token(payload, timeout=1):
    import jwt
    import datetime

    # header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)

    token = jwt.encode(payload=payload, key=salt, headers=headers)
    return token


def valid_token(request):
    try:
        import json
        body = json.loads(request.get_data(as_text=True))
        token = body['token']

    except BaseException:
        return {
            'code': 1003,
            'message': '{}: Please login in'.format(custom_status_code[1003])
        }

    import jwt
    payload = None
    error_msg = None
    try:
        payload = jwt.decode(token, salt, 'HS256')
    except jwt.ExpiredSignatureError:
        error_msg = 'Token is timeout'
    except jwt.DecodeError:
        error_msg = 'Token validation failed'
    except jwt.InvalidTokenError:
        error_msg = 'Token is invalid'

    if not payload:
        return {
            'code': 1003,
            'message': error_msg
        }
    return {
        'code': 1002,
        'message': custom_status_code[1002]
    }


def valid_authority(provide, request):
    switcher = {
        0: 'guest',
        1: 'admin',
        2: 'superAdmin'
    }

    if str(type(provide)) == "<class 'int'>":
        provide = switcher[provide]
    if str(type(request)) == "<class 'int'>":
        request = switcher[request]

    if authority[provide] < authority[request]:
        return {
            'code': 1201,
            'message': custom_status_code[1201]
        }
    return {
        'code': 1200,
        'message': custom_status_code[1200]
    }


