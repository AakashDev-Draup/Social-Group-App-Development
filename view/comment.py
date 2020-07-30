from flask import request
from model.models import User, Group, Post, Comment
from flask_restful import Resource
from bson import ObjectId
from datetime import datetime
# from mail.mail import send_email
# from queue_tasks.task import funcqueue


class CommentApi(Resource):
    # Update last active status for the user who commented
    # Only group users can comment

    def post(self, groupid,postid):
        # body contains user id,content
        body = request.get_json()
        user = User.objects.get(id=body['userid'])
        group = Group.objects.get(id=groupid)
        if body['userid'] in group.role_dict:
            comment = Comment(**body, postid=ObjectId(postid))
            comment.date_created = datetime.now()
            comment.save()
            # update last active status for user
            temp_dict = group.lastactive_dict
            temp_dict[body['userid']] = datetime.now()
            group.update(set__lastactive_dict=temp_dict)
            # this sends mail to the post owner
            # funcqueue(send_email('Post Update', 'socialgroup.co.in', user.email, comment.content))
            return {'commentid': str(comment.id)}, 200
        else:
            return "You are not a member of the group", 200


class DeleteCommentApi(Resource):
    # only post owner, admin and moderator can delete
    def delete(self, groupid,commentid):
        # body contains user id
        body = request.get_json()

        comment = Comment.objects.get(id=commentid)
        group = Group.objects.get(id=groupid)
        try:
            role = group.role_dict[body['userid']]
            comments = Comment.objects(userid=body['userid'])
            if comment in comments or role == 'ADMIN' or role == 'MODERATOR':
                comment.delete()
                return "Comment deleted", 200
            else:
                return "You don't have the permission required", 200
        except:
            return "You are not a member of the group", 200

