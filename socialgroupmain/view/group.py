from flask import Response, request
from mongoengine import Q

from socialgroupmain.auth_module.auth_main import auth

from socialgroupmain.model.models import Group, Post, User,Comment
from flask_restful import Resource
from datetime import datetime
from socialgroupmain import constants


class DeleteGroupApi(Resource):
    @auth.login_required
    def delete(self,groupid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        group = Group.objects.get(id=groupid)
        if group.role_dict[uid] in constants.admin:
            group.delete()
            for post in Post.objects(groupid=groupid):
                postid = post.id
                post.delete()
                Comment.objects(postid=postid).delete()
            return "Group deleted successfully", 200
        else:
            return "You do not have the required access",500


class EditGroupApi(Resource):
    @auth.login_required
    def put(self,groupid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        # body contains the name and visibility to be edited
        body = request.get_json()
        group = Group.objects.get(id=groupid)
        if group.role_dict[uid] in constants.admin:
            if 'name' and 'visibility' in body:
                name = body['name']
                visibility = body['visibility']
                group.update(set__name=name)
                group.update(set__visibility=visibility)
                group = group.to_json()
                return Response(group, mimetype="application/json", status=200)
            else:
                name = body['name']
                group.update(set__name=name)
                group = group.to_json()
                return Response(group, mimetype="application/json", status=200)
        else:
            return "You do not have the required access", 500


class GetGroupApi(Resource):

    @auth.login_required
    def get(self,groupid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        try:
            group = Group.objects.get(id=groupid)
            if uid in group.role_dict:
                group = Group.objects(id=groupid).to_json()
                return Response(group, mimetype="application/json", status=200)
            else:
                return "You are not member of the group", 500
        except Exception as e:
            return e


class ReadGroupApi(Resource):
    # read group contents based on access offered by group i.e. public or private
    # and also based on post approval
    @auth.login_required
    def get(self,groupid):
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        try:
            group = Group.objects.get(id=groupid)

            if group.visibility == 'public':
                posts = Post.objects(Q(groupid=group.id) & Q(approval=True)).to_json()
                return Response(posts, mimetype="application/json", status=200)
            elif uid in group.role_dict:
                posts = Post.objects(Q(groupid=group.id) & Q(approval=True)).to_json()
                return Response(posts, mimetype="application/json", status=200)
            else:
                return "You do not have the required access", 200

        except Exception as e:
            return e


class CreateGroupApi(Resource):
    # first user is the ADMIN
    # create group
    @auth.login_required
    def post(self):
        # body has visibility = (default= public) and name of group
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        body = request.get_json()

        group = Group(**body)
        group.role_dict[uid] = 'ADMIN'
        group.save()
        groupid = group.id
        return {'groupid': str(groupid)}, 200


class AddUserGroupApi(Resource):
    @auth.login_required
    # only ADMIN can add user
    def put(self, groupid):
        # body will have dict with id and role for new join
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        body = request.get_json()

        nuser = body['adduser']     # dict with {'userid':'role'} ex : {'adsfdsfds':'MEMBER'}
        nuserid = list(nuser.keys())[0]
        group = Group.objects.get(id=groupid)
        temp = group.role_dict
        temp.update(nuser)
        tempdict = group.lastactive_dict
        # this temp dict is for last active update
        if uid in group.role_dict and group.role_dict[uid] == 'ADMIN':
            group.update(set__role_dict=temp)
            tempdict[nuserid]=datetime.now()
            group.update(set__lastactive_dict=tempdict)
            return "User admitted successfully", 200
        else:
            return "Admin access denied"


class RemoveUserGroupApi(Resource):

    @auth.login_required
    # only ADMIN can remove user
    def put(self,groupid):
        # body will have id of user to be removed
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)
        body = request.get_json()

        group = Group.objects.get(id=groupid)
        try:
            if group.role_dict[uid] == 'ADMIN':
                deluser = body['deleteuser']

                role_dict = group.role_dict
                lastactive_dict = group.lastactive_dict
                for key in list(role_dict):
                    if key == deluser:
                        del role_dict[deluser]
                        break
                # element should be deleted in dict via this way otherwise iteration error
                for key in list(lastactive_dict):
                    if key == deluser:
                        del lastactive_dict[deluser]
                        break
                group.update(set__lastactive_dict=lastactive_dict)
                group.update(set__role_dict=role_dict)
                return "user deleted successfully" , 200
            else:
                return "You are not an ADMIN" , 200
        except:
            return "You are not a member of the group" , 200


class ChangeRoleApi(Resource):
    # only admin can change role
    @auth.login_required
    def put(self,groupid):

        # body contains dict of person whose role is changed {"user id":"new role"}
        user = request.authorization
        uid = User.objects.get(name=user['username'])
        uid = str(uid.id)

        body = request.get_json()

        group = Group.objects(id=groupid).get()
        try:
            if group.role_dict[uid] == 'ADMIN':
                role_dict = group.role_dict
                role_dict.update(body['changerole'])
                group.update(set__role_dict=role_dict)
                return "Role changed successfully",200
            else:
                return "You are not an admin",200
        except:
            return "You are not member of the group",200







