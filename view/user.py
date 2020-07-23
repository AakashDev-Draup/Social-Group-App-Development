from flask import Response, request
from model.models import User
from flask_restful import Resource


class Userapi(Resource):

    # create group
    def post(self):
        body = request.get_json()
        user = User(**body).save()
        userid = user.id
        return {'userid': str(userid)}, 200

    #add user edit post
    #user delete post
    #user comment
    #user delete comment
