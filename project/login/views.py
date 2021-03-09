from flask import request
from flask_restful import Resource, fields, marshal
from .models import User
import json
from ..utils import custom_status_code


class UserView(Resource):
    user_fields = {
        'authority': fields.String(attribute='uauthority'),
        'username': fields.String(attribute='username')
    }

    def post(self):
        # raw | form-data
        data = json.loads(request.get_data(as_text=True))
        email = data['email']
        pwd = data['password']

        user_object = User.query.filter_by(email=email, upassword=pwd).first()
        if not user_object:
            return {
                'code': 1001,
                'message': custom_status_code[1001]
            }

        data = marshal(user_object, UserView.user_fields)
        from ..utils.authority import create_token
        token = create_token({'data': data}, 60*24*7)
        data['token'] = token
        return {
            'code': 1000,
            'data': data,
            'message': custom_status_code[1000]
        }




