from socialgroupmain.auth_module.auth_main import SignupApi
from socialgroupmain.view.group import CreateGroupApi, AddUserGroupApi, RemoveUserGroupApi, ReadGroupApi,ChangeRoleApi,GetGroupApi
from socialgroupmain.view.post import PostApi,DeletePostApi,GetPostApi
from socialgroupmain.view.comment import CommentApi,DeleteCommentApi,GetCommentApi


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/signup')                                              # signup user
    api.add_resource(CreateGroupApi, '/api/group/create')                                   # create group
    api.add_resource(AddUserGroupApi, '/api/group/<groupid>/add/user')                      # add user to the group
    api.add_resource(PostApi, '/api/group/<groupid>/post/add')                              # add post
    api.add_resource(ReadGroupApi, '/api/group/<groupid>/read')                             # read posts from group
    api.add_resource(RemoveUserGroupApi, '/api/group/<groupid>/remove/user')                # Remove user from the group
    api.add_resource(CommentApi, '/api/group/<groupid>/post/<postid>/comment/add')          # add comment
    api.add_resource(DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')            # delete post
    api.add_resource(DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete')   # delete comment
    api.add_resource(ChangeRoleApi, '/api/group/<groupid>/changerole')                      # change user role

    api.add_resource(GetGroupApi, '/api/group/<groupid>')                                   # get the group by id
    api.add_resource(GetPostApi, '/api/group/<groupid>/post/<postid>')                      # get the post by id
    api.add_resource(GetCommentApi, '/api/group/<groupid>/comment/<commentid>')             # get the comment by id
