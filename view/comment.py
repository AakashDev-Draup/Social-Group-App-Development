from flask import Response, request
from model.models import User, Group, Post, Comment
from flask_restful import Resource
from bson import ObjectId



class commentapi(Resource):

    # create comment and update in user list
    # Only group users can comment
    # / api /<gid>/<pid>/comment
    def post(self,gid,pid):
        # gid is group id,pid post id and body contains Comment class contents
        body = request.get_json()
        userid = body['userid']
        group = Group.objects.get(id=gid)
        for user in group.users:
            if userid in user:
                comment = Comment(**body, postid=ObjectId(pid)).save()
                # post id is a reference field and rf only takes object id.
                # convert object id to string with str when required
                commentid = comment.id
                # change user list
                User.objects(id=userid).update_one(push__comments=comment)
                return {'commentid': str(commentid)}, 200
        return 'You are not a member of the group'


    # user delete comment
    # user comment