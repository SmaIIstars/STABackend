# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @version: v3.7
# @author: Small_stars
# @mailbox: smallstars.he@qq.com
# @site: 
# @software: PyCharm
# @file: email.py
# @time: 2021/1/23 17:15
from flask import request
import json
import random
import yagmail
import time
import hashlib


def routes(app):
    @app.route('/data/captcha', methods=['POST'])
    def email_captcha():
        time_stamp = time.time()
        data = json.loads(request.get_data(as_text=True))
        username, user_email = [data['username'], data['email']]
        captcha = generate_captcha(6)
        from ..utils import from_email
        yag = yagmail.SMTP(
            user=from_email['user'],
            password=from_email['password'],
            host=from_email['host']
        )
        subject = ['CDUT STA 验证码']
        contents = generate_contents(username, captcha)
        hash_value = hashlib.sha512((str(time_stamp)+captcha).encode('utf-8'))

        # yag.send(user_email, subject, contents)
        print("[captcha.py 36 line] captcha: {}".format(captcha))
        return {
            "time": time_stamp,
            "captcha": hash_value.hexdigest()
        }


def generate_captcha(size):
    res = ''
    for i in range(size):
        res += str(random.randint(0, 9))
    return res


def generate_contents(username, code):
    return ['''
<table width="600" cellspacing="0" border="0" align="center" style="border: rgba(0, 0, 0, 0.3) 1px solid">
  <tbody style="align-items: center">
    <tr style=" height: 64px; background-color: #415a94; color: #fff;">
      <td style="text-align: center; font-size: 21px;">CDUT STA</td>
    </tr>

    <tr>
      <td style=" display: table-cell; padding: 8% 0; color: #000; text-align: center; font-size: 21px; ">
        邮箱验证码
      </td>
    </tr>

    <tr>
      <td style="display: table-cell; padding: 0 6%; color: #333">
        尊敬的 {} , 您好！
      </td>
    </tr>

    <tr>
      <td style="display: table-cell; padding: 2% 6% 10% 6%; color: #333">
          您的验证码是: <span style="font-weight: 600; color: red">{}</span> ,请在 5 分钟内进行验证。如果该验证码不为您本人申请,请无视。
      </td>
    </tr>

    <tr>
      <td style="background: #f7f7f7; display: table-cell; padding: 2% 6%">
        <a href="https://www.baidu.com" style="color: #929292">返回</a>
      </td>
    </tr>
  </tbody>
</table>'''.format(username, code).replace('\n', '')]

