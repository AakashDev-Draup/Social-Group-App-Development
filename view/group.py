from flask import Response, request
from model.models import Group,Role
from flask_restful import Resource


class Groupapi(Resource):

    # create group
    def post(self,id):
        # id is the userid of group creator
        body = request.get_json()
        group = Group(**body)
        group.users = [{id:'ADMIN'}]
        group.save()
        groupid = group.id
        return {'groupid': str(groupid)}, 200


class addtogroupapi(Resource):

    # push user to the group by roles who have add rights
    def put(self, id):
        # id is group id here
        # body will have userid of both admin and new join
        body = request.get_json()
        uid = body['userid']
        nuser = body['newuser']     # dict with {'userid':'role'} ex : {'adsfdsfds':'MEMBER'}
        group = Group.objects.get(id=id)
        for user in group.users:
            if uid in user:
                permission = Role.objects.get(name=user[uid])
                permission = permission.permissions
                if 'ADDUSER' in permission:
                    group.update(push__users=nuser)
                    return 'User added successfully'
                else:
                    return "You don't have add user rights"

        return 'Person adding user is not a member of the group'

class removegroupapi(Resource):

    # pull user from the group by roles who have remove from group rights
    def put(self,id):
        # id is group id here
        # body will have userid of both admin and user to be deleted
        body = request.get_json()
        uid = body['userid']
        duser = body['deluser']             # dict with {'userid':'role'} ex : {'adsfdsfds':'MEMBER'}
        group = Group.objects.get(id=id)
        for user in group.users:
            if uid in user:
                permission = Role.objects.get(name=user[uid])
                permission = permission.permissions
                if 'DELUSER' in permission:
                    group.update(pull__users=duser)
                    return 'User Removed successfully'
                else:
                    return "You don't have delete user rights"

        return 'Person removing user is not a member of the group'



    # # show all posts only for member
    # use public private concept here
    # def get(self,id):


    # change role of user in group only admin
    #delete group

    # def delete(self, groupid):
    #     body = request.get_json()
    #     group = Group.objects(id=groupid).update(**body)
    #     return ''





