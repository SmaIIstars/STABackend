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
    def emailCaptcha():
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
        print(hash_value.hexdigest())
        print((str(time_stamp)+captcha))

        return {
            "time": time_stamp,
            "code": hash_value.hexdigest()
        }


def generate_captcha(size):
    res = ''
    for i in range(size):
        res += str(random.randint(0, 9))
    return res


def generate_contents(username, code):
    return '''
        <table style="width: 99.8%; height: 95%;">
            <tbody>
                <tr>
                    <td id="QQMAILSTATIONERY" style="background:url(https://rescdn.qqmail.com/bizmail/zh_CN/htmledition/images/xinzhi/bg/a_02.jpg) no-repeat #fffaf6; min-height:550px; padding:100px 55px 200px 100px; ">
                    <div style="text-align: center;"><font>{},您好！&nbsp;</font></div>
                    <div style="text-align: center;"><font><br>
                        </font>
                    </div>
                    <div style="text-align: center;"><font>您的 JunJun.Tec 验证码/临时登录密码 为&nbsp;</font></div>
                    <div style="text-align: center;"><font><br>
                        </font>
                    </div>
                    <div style="text-align: center;"><font color="#ff0000"><b><u>{}</u></b></font></div>
                    <div style="text-align: center;"><font><br>
                        </font>
                    </div>
                    <div style="text-align: center;"><font>如非您本人操作无需理会。&nbsp;</font></div>
                    <div style="text-align: center;"><font><br>
                        </font>
                    </div>
                    <div style="text-align: center;"><font>感谢支持。</font></div>
                    </td>
                </tr>
            </tbody>
        </table>
        <div><includetail><!--<![endif]--></includetail></div>
        '''.format(username, code)

