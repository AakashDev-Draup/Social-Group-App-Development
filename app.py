
from flask import Flask, request, Response
from configs.config import initialize_db
from model.models import Permissions, User, Roles, Group, Post, Comment
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Social-Group'
}

initialize_db(app)


#  permissions
@app.route('/group/permissions', methods=['POST'])
def add_permission():
    body = request.get_json()
    permission = Permissions(**body).save()
    permissionid = permission.id
    return {'permissionid': str(permissionid)}, 200


#add role
@app.route('/role', methods=['POST'])
def add_role():
    body = request.get_json()
    role = Roles(**body).save()
    roleid = role.id
    return {'roleid': str(roleid)}, 200


# create group
@app.route('/group', methods=['POST'])
def add_group():
    body = request.get_json()
    group = Group(**body).save()
    groupid = group.id
    return {'groupid': str(groupid)}, 200


#create user
@app.route('/user', methods=['POST'])
def add_user():
    body = request.get_json()
    user = User(**body).save()
    userid = user.id
    return {'userid': str(userid)}, 200


#create post
@app.route('/group/<id>/post', methods=['POST'])
def add_post():
    body = request.get_json()
    post = Post(**body).save()
    postid = post.id
    return {'postid': str(postid)}, 200


#create comment
@app.route('/post/<id>/comment', methods=['POST'])
def add_comment():
    body = request.get_json()
    post = Comment(**body).save()
    commentid = comment.id
    return {'commentid': str(commentid)}, 200

