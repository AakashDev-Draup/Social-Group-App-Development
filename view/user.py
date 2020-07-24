from flask import request
from model.models import User
from flask_restful import Resource


class Userapi(Resource):

    # create user
    def post(self):
        body = request.get_json()
        user = User(**body).save()
        userid = user.id
        return {'userid': str(userid)}, 200
