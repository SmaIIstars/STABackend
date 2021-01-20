# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: token.py
# @time: 2021/1/20 14:15
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
    print(payload)

    token = jwt.encode(payload=payload, key=salt, headers=headers)
    return token


def valid_token(request):
    try:
        token = request.form['token']

    except BaseException:
        return {
            'code': 1003,
            'error': 'Please login in'
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
            'error': error_msg
        }
    return {
        'code': 1002
    }


