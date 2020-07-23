from bson import ObjectId
from flask import Response, request
from model.models import User,Group,Post
from flask_restful import Resource



class postapi(Resource):

    # create post and update in user list
    # group users can post only such authentication is required
    # / api / Group / < id > / post
    def post(self,id):
        body = request.get_json()
        post = Post(**body, groupid=ObjectId(id)).save()
        # mongo reference field only takes object id convert with str when required
        postid = post.id
        userid = body['userid']
        # updates user list for post

        user = User.objects(id=userid).update_one(push__posts=post)

        return {'postid': str(postid)}, 200


    #admin moderator delete post