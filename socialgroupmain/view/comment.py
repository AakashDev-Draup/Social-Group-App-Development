from flask import request,Response
from socialgroupmain.model.models import User, Group, Post, Comment
from flask_restful import Resource
from bson import ObjectId
from datetime import datetime
from socialgroupmain.configuration.config import queue
from socialgroupmain.mail_module.mail_functions import send_mail
from socialgroupmain.queue_tasks.checkq import printhello
from socialgroupmain.auth_module.auth_main import auth


class GetCommentApi(Resource):
    @auth.login_required
    def get(self,commentid,groupid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        try:
            group = Group.objects.get(id=groupid)
            if uid in group.role_dict:
                comment = Comment.objects(id=commentid).to_json()
                return Response(comment, mimetype="application/json", status=200)
            else:
                return "You are not member of the group", 500
        except:
            return "Invalid group or comment id", 500


class CommentApi(Resource):
    # Update last active status for the user who commented
    # Only group users can comment

    @auth.login_required
    def post(self, groupid,postid):
        # body contains content
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        body = request.get_json()
        user = User.objects.get(id=uid)
        group = Group.objects.get(id=groupid)
        if uid in group.role_dict:
            comment = Comment(**body, postid=ObjectId(postid),userid=user)
            comment.date_created = datetime.now()
            comment.save()
            # update last active status for user
            temp_dict = group.lastactive_dict
            temp_dict[uid] = datetime.now()
            group.update(set__lastactive_dict=temp_dict)
            # this sends mail to the post owner
            content = "{a} posted a comment today".format(a=user.name)
            queue.enqueue(printhello)     # this is just a check that queuing works
            queue.enqueue(send_mail,[user.email],content)
            return {'commentid': str(comment.id)}, 200
        else:
            return "You are not a member of the group", 200


class DeleteCommentApi(Resource):
    # only post owner, admin and moderator can delete
    @auth.login_required
    def delete(self, groupid,commentid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        comment = Comment.objects.get(id=commentid)
        group = Group.objects.get(id=groupid)
        try:
            role = group.role_dict[uid]
            comments = Comment.objects(userid=uid)
            if comment in comments or role == 'ADMIN' or role == 'MODERATOR':
                comment.delete()
                return "Comment deleted", 200
            else:
                return "You don't have the permission required", 200
        except:
            return "You are not a member of the group", 200

