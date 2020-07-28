from auth.auth import SignupApi
from view.group import CreateGroupApi, AddUserGroupApi, RemoveUserGroupApi, ReadGroupApi
from view.post import PostApi,DeletePostApi
from view.comment import CommentApi,DeleteCommentApi


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/signup')                          # signup user
    api.add_resource(CreateGroupApi, '/api/group/create')               # create group
    api.add_resource(AddUserGroupApi, '/api/group/<groupid>/add')       # add user to the group
    api.add_resource(PostApi, '/api/group/<groupid>/post/add')          # add post
    api.add_resource(ReadGroupApi, '/api/group/<groupid>/read')         # read posts from group
    api.add_resource(RemoveUserGroupApi, '/api/group/<groupid>/remove')   # Remove user from the group
    api.add_resource(CommentApi, '/api/group/<groupid>/post/<postid>/comment/add')        # add comment
    api.add_resource(DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')          # delete post
    api.add_resource(DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete')     # delete comment)

