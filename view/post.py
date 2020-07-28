from bson import ObjectId
from flask import request
from model.models import User,Group,Post,Role
from flask_restful import Resource
from datetime import datetime


class PostApi(Resource):

    # Update last active status for the user who posted
    # Only group users can post

    def post(self,groupid):
        # body contains user id,content
        body = request.get_json()
        group = Group.objects.get(id=groupid)
        if body['userid'] in group.role_dict:
            post = Post(**body, groupid=ObjectId(groupid))
            post.date_created = datetime.now()
            post.save()
            # group id is a reference field and rf only takes object id.
            # convert object id to string with str when required
            # update last active status for user
            temp_dict = group.lastactive_dict
            temp_dict[body['userid']]=datetime.now()
            group.update(set__lastactive_dict=temp_dict)

            return {'postid': str(post.id)}, 200
        else:
            return "You are not a member of the group",200


class DeletePostApi(Resource):
    # only post owner, admin and moderator can delete
    def delete(self,groupid,postid):
        # body contains user id
        body = request.get_json()
        post = Post.objects.get(id=postid)
        group = Group.objects.get(id=groupid)
        role = group.role_dict[body['userid']]
        if post.userid == body['userid'] or role == 'ADMIN' or role == 'MODERATOR':
            post.delete()
            return "Post deleted",200
        else:
            return "You don't have the permission required" , 200