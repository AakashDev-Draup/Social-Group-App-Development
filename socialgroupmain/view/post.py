from bson import ObjectId
from flask import request,Response
from socialgroupmain import constants
from socialgroupmain.configuration.config import queue
from socialgroupmain.mail_module.mail_functions import send_mail
from socialgroupmain.model.models import User,Group,Post
from flask_restful import Resource
from datetime import datetime
from socialgroupmain.auth_module.auth_main import auth
from socialgroupmain.queue_tasks.checkq import printhello


class ApprovePostApi(Resource):
    @auth.login_required
    def put(self,groupid,postid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        # body contains the approval = True
        body = request.get_json()
        group = Group.objects.get(id=groupid)
        temp = group.role_dict
        post = Post.objects.get(id=postid)
        if temp[uid] in constants.group_permissions:
            post.update(set__approval=True)
            post = post.to_json()
            return "successfully approved" , 500

        else:
            return "User doesn't have access", 500


class EditPostApi(Resource):
    @auth.login_required
    def put(self,groupid,postid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        # body contains the new content for post
        body = request.get_json()

        post = Post.objects.get(id=postid)
        group = Group.objects.get(id=groupid)
        temp = group.role_dict
        lastdict = group.lastactive_dict

        if uid == str(post.userid) or temp[uid] in constants.group_permissions:
            lastdict[uid] = datetime.now()
            group.update(set__lastactive_dict=lastdict)
            post.update(set__content=body['content'])
            post = post.to_json()
            return Response(post, mimetype="application/json", status=200)

        else:
            return "User doesn't exist or doesn't have access", 500


class GetPostApi(Resource):
    @auth.login_required
    def get(self,groupid,postid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        try:
            group = Group.objects.get(id=groupid)
            if uid in group.role_dict:

                post = Post.objects.get(id=postid).to_json()

                return Response(post, mimetype="application/json", status=200)

            else:
                return "You are not member of the group", 500
        except:
            return "Invalid group or post id", 500


class PostApi(Resource):

    # Update last active status for the user who posted
    # Only group users can post
    @auth.login_required
    def post(self,groupid):
        # body contains content
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        body = request.get_json()
        group = Group.objects.get(id=groupid)
        if uid in group.role_dict:
            post = Post(**body, groupid=ObjectId(groupid),userid=ObjectId(uid))
            post.date_created = datetime.now()
            post.save()
            # group id is a reference field and rf only takes object id.
            # convert object id to string with str when required
            # update last active status for user
            temp_dict = group.lastactive_dict
            temp_dict[uid]=datetime.now()
            group.update(set__lastactive_dict=temp_dict)
            # for sending mail to admin and moderators for approval if member
            if group.role_dict[uid] in constants.member:
                recipients = []
                for userid, access in group.role_dict.items():
                    if access in constants.group_permissions:
                        user = User.objects.get(id=userid)
                        recipients.append(user.email)
                subject = 'Post is pending for approval'
                mail_content = '''Post id : {pid} , Group id : {gid}\n
                Thank you\n
                The Social-Group Team'''.format(pid=post.id,gid=groupid)
                # queue.enqueue(printhello)
                queue.enqueue(send_mail, mail_content, recipients, subject)
            else:
                post.update(set__approval=True)
            return {'postid': str(post.id)}, 200
        else:
            return "You are not a member of the group",200


class DeletePostApi(Resource):
    # only post owner, admin and moderator can delete
    @auth.login_required
    def delete(self,groupid,postid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        post = Post.objects.get(id=postid)
        group = Group.objects.get(id=groupid)
        try:
            role = group.role_dict[uid]
            posts = Post.objects(userid=uid)
            if post in posts or role == 'ADMIN' or role == 'MODERATOR':
                post.delete()
                return "Post deleted",200
            else:
                return "You don't have the permission required" , 200
        except:
            return "You are no longer member of the group", 200