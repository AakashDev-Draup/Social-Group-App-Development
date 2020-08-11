from socialgroupmain.auth_module.auth_main import SignupApi,GetUserApi,DeleteUserApi
from socialgroupmain.view.group import CreateGroupApi, AddUserGroupApi, RemoveUserGroupApi,\
    ReadGroupApi,ChangeRoleApi,GetGroupApi,EditGroupApi,DeleteGroupApi
from socialgroupmain.view.post import PostApi,DeletePostApi,GetPostApi,EditPostApi,ApprovePostApi
from socialgroupmain.view.comment import CommentApi,DeleteCommentApi,GetCommentApi,EditCommentApi,AllCommentsApi


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/signup')                                              # signup user
    api.add_resource(CreateGroupApi, '/api/group/create')                                   # create group
    api.add_resource(AddUserGroupApi, '/api/group/<groupid>/add/user')                      # add user to the group
    api.add_resource(PostApi, '/api/group/<groupid>/add/post')                              # add post
    api.add_resource(ReadGroupApi, '/api/group/<groupid>/read')                             # read posts from group
    api.add_resource(RemoveUserGroupApi, '/api/group/<groupid>/remove/user')                # Remove user from the group
    api.add_resource(CommentApi, '/api/group/<groupid>/post/<postid>/add/comment')          # add comment
    api.add_resource(DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')            # delete post
    api.add_resource(DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete')   # delete comment
    api.add_resource(ChangeRoleApi, '/api/group/<groupid>/changerole')                      # change user role
    api.add_resource(EditCommentApi, '/api/group/<groupid>/comment/<commentid>/edit')  # edit comment

    api.add_resource(EditPostApi, '/api/group/<groupid>/post/<postid>/edit')  # Edit the post
    api.add_resource(GetGroupApi, '/api/group/<groupid>')                                   # get the group by id
    api.add_resource(GetPostApi, '/api/group/<groupid>/post/<postid>')                      # get the post by id
    api.add_resource(GetCommentApi, '/api/group/<groupid>/comment/<commentid>')             # get the comment by id
    api.add_resource(GetUserApi, '/api/user')  # get user by id
    api.add_resource(EditGroupApi, '/api/group/<groupid>/edit')  # edit group name or visibility
    api.add_resource(ApprovePostApi, '/api/group/<groupid>/post/<postid>/approve')  # Approve the post
    api.add_resource(AllCommentsApi, '/api/group/<groupid>/post/<postid>/comments')  # get all the comments for a post
    api.add_resource(DeleteUserApi, '/api/delete/user')
    api.add_resource(DeleteGroupApi, '/api/group/<groupid>/delete')
