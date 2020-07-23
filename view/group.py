from flask import Response, request
from model.models import Group, groupuser, User
from flask_restful import Resource


class Groupapi(Resource):

    # create group
    def post(self):
        body = request.get_json()
        group = Group(**body).save()
        groupid = group.id
        return {'groupid': str(groupid)}, 200


class editgroupapi(Resource):

    # push user to the group by admin or moderator
    # authorisation yet to be added
    def put(self, id):
        body = request.get_json()
        member = groupuser(**body)
        group = Group.objects(id=id).update_one(push__users=member)

        # usergroupupdate = User.objects(id=member.userid).update_one(push__groups=id)

        return ''



    # # pull user from the group by admin or moderator
    # # authorisation yet to be added
    # def delete(self, groupid):
    #     body = request.get_json()
    #     group = Group.objects(id=groupid).update(**body)
    #     return ''





