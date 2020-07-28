from flask import request
from model.models import Role,User
from flask_restful import Resource


# Sign up page for user
class SignupApi(Resource):
    def post(self):
        # name and email is supplied in body
        body = request.get_json()
        user = User(**body).save()
        userid = user.id
        return {'userid': str(userid)}, 200


# not using this for now

# class CreateRole(Resource):
#     # ADMIN create roles and assign the permissions
#     # admin userid , role name and permissions in the body
#     def post(self):
#         body = request.get_json()
#         userid = body['userid']
#         user = User.objects(id=userid)
#         if user.role_dict[userid]=='ADMIN':
#             role = Role(body['name'],body['permissions']).save()
#             return "Role created", 200
#         else:
#             return "You are not an ADMIN", 200

