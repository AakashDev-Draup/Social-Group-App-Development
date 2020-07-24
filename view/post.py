from bson import ObjectId
from flask import Response, request
from model.models import User,Group,Post
from flask_restful import Resource



class postapi(Resource):

    # create post and update in user list and group list
    # Only group users can post
    # / api / Group / < id > / post
    def post(self,id):
        # id is group id and body contains Post class contents
        body = request.get_json()
        userid = body['userid']
        group = Group.objects.get(id=id)
        for user in group.users:
            if userid in user:
                post = Post(**body, groupid=ObjectId(id)).save()
                # group id is a reference field and rf only takes object id.
                # convert object id to string with str when required
                postid = post.id
                # change user list
                User.objects(id=userid).update_one(push__posts=post)
                # change group list
                group.update(push__posts=post)
                return {'postid': str(postid)}, 200
        return 'You are not a member of the group'



    #update posts in group
    #admin moderator delete ANY post
    # add user edit post
    # user delete post