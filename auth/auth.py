from flask import request
from model.models import Role
from flask_restful import Resource


class roleapi(Resource):
    # create roles and adds all the permissions

    def post(self,id):
        if id == 'ae123bg':
            body = request.get_json()
            role = Role(**body).save()
            roleid = role.id
            return {'roleid': str(roleid)}, 200



