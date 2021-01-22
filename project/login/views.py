from flask import request
from flask_restful import Resource, fields, marshal
from .models import User
import json


class UserView(Resource):
    user_fields = {
        'name': fields.String(attribute='username'),
        'authority': fields.String(attribute='uauthority'),
    }

    def post(self):
        # raw | form-data
        data = json.loads(request.get_data(as_text=True))
        name = data['username']
        pwd = data['password']

        user_object = User.query.filter_by(username=name, upassword=pwd).first()
        if not user_object:
            return {
                'code': 1000,
                'message': 'Username or password error'
            }

        data = marshal(user_object, UserView.user_fields)
        from ..utils.token import create_token
        token = create_token({'data': data}, 60)
        data['token'] = token
        return {
            'code': 1001,
            'data': data,
            'message': 'login successful'
        }




