from flask import request, Response
from socialgroupmain.model.models import User
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if User.objects.filter(name=username).first():
        user = User.objects.filter(name=username).first()
        if check_password_hash(user.password, password):
            return True

# Sign up page for user


class SignupApi(Resource):
    def post(self):
        # name and email is supplied in body
        try:
            body = request.get_json()
            body['password'] = generate_password_hash(body['password'])
            user = User(**body).save()
            userid = user.id
            return {'userid': str(userid)}, 200
        except:
            return "username should be unique try again",500


class GetUserApi(Resource):
    @auth.login_required
    def get(self):
        user = request.authorization
        uid = User.objects(name=user['username']).to_json()

        return Response(uid, mimetype="application/json", status=200)




