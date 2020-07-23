from flask import Response, request
from model.models import User, Group, Post, Comment
from flask_restful import Resource
from bson import ObjectId



class commentapi(Resource):

    # create comment and update in user list
    # / api / post / < id > / comment
    def post(self,id):
        body = request.get_json()
        comment = Comment(**body, postid=ObjectId(id)).save()
        commentid = comment.id

        userid = body['userid']
        # updates user list for comments

        user = User.objects(id=userid).update_one(push__comments=comment)
        return {'commentid': str(commentid)}, 200

    # user delete comment