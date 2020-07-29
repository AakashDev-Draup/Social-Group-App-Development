from flask import Response, request
from model.models import Group,Role,Post
from flask_restful import Resource
from datetime import datetime


class ReadGroupApi(Resource):
    # read group contents based on access offered by group i.e. public or private
    def get(self,groupid):
        # body will have userid of person accessing to read
        body = request.get_json()
        userid = body['userid']
        group = Group.objects.get(id=groupid)

        if group.visibility == 'public':
            posts = Post.objects(groupid=groupid).to_json()
            return Response(posts, mimetype="application/json", status=200)
        elif userid in group.role_dict:
            posts = Post.objects(groupid=groupid).to_json()
            return Response(posts, mimetype="application/json", status=200)
        else:
            return "You do not have the required access", 200


class CreateGroupApi(Resource):
    # first user is the ADMIN
    # create group
    def post(self):
        # body has id of group creator
        body = request.get_json()
        userid = body['userid']
        name = body['userid']
        if body['visibility']:
            visibility = body['visibility']
        else:
            visibility = 'public'
        group = Group(name=name,visibility=visibility)
        group.role_dict[userid] = 'ADMIN'
        group.save()
        groupid = group.id
        return {'groupid': str(groupid)}, 200


class AddUserGroupApi(Resource):

    # only ADMIN can add user
    def put(self, groupid):
        # body will have userid of admin and dict with id and role for new join
        body = request.get_json()
        uid = body['userid']
        nuser = body['newuser']     # dict with {'userid':'role'} ex : {'adsfdsfds':'MEMBER'}
        nuserid = list(nuser.keys())[0]
        group = Group.objects.get(id=groupid)
        nuser.update(group.role_dict)
        tempdict = group.lastactive_dict
        # this temp dict is for last active update
        if uid in group.role_dict and group.role_dict[uid] == 'ADMIN':
            group.update(set__role_dict=nuser)
            tempdict[nuserid]=datetime.now()
            group.update(set__lastactive_dict=tempdict)
            return "User admitted successfully", 200
        else:
            return "Admin access denied"


class RemoveUserGroupApi(Resource):

    # only ADMIN can remove user
    def put(self,groupid):
        # body will have userid of admin and id of user to be removed

        body = request.get_json()
        uid = body['userid']
        group = Group.objects.get(id=groupid)
        try:
            if group.role_dict[uid] == 'ADMIN':
                deluser = body['deluserid']

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



