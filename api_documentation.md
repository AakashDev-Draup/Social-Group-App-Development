##List of APIS

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

##Description

_Note : Format in which data is supplied through the body of the request is shown with examples below._

###(SignupApi, '/api/signup')

This is the first thing you need to do for accessing the social group app, you have to signup using your name,
a password, and an email id. In the body of the request put the name, password, and email. The response will 
return an user id which you have to use for future use.

For ex : Body
{
"name":"aakash",
"password":"12340",
"email":"blah@gmail.com"
}

_Note : After signup authorisation is needed in all the APIs. Use your username and password in the authorisation
tab before submitting the request._

###(CreateGroupApi, '/api/group/create')

After you signup you can create your group using this api. As you created the group you will be the admin of the
group and you will have the rights to add user and change their roles. The body of the request will contain the
user id, the name of the group, and the visibility. By default the visibility is public.

For ex : Body
{
"userid":"asdfadsfdsfds54564156",
"name":"Test group",
"visibility":"private"
}

###(AddUserGroupApi, '/api/group/<groupid>/add/user')  

This api is used for adding member to the group. The user adding the member should be an admin. The body of the 
request will contain the user id of the user adding the member and a dictionary containing user id of the member being
added to the group and his role between 'ADMIN', 'MEMBER', and 'MODERATOR'.

For ex : Body
{
"userid":"asdfadsfdsfds54564156",
"newuser":{"dfdfasdfdsf":"MEMBER"}
} 

###(RemoveUserGroupApi, '/api/group/<groupid>/remove/user')

This api is used to remove user from the group. The body of the request contains the user id of one of the admins of
 group and user id of the member being removed.
 
 For ex : Body
{
"userid":"asdfadsfdsfds54564156",
"deluserid":"dsfgdfgfhfghfghfg"
} 

###(PostApi, '/api/group/<groupid>/post/add')

This API is used to create a post. The body contains the user id of the post owner and content.
The user creating the post must be member of the group.

 For ex : Body
{
"userid":"asdfadsfdsfds54564156",
"content":"my first post"
} 

###(CommentApi, '/api/group/<groupid>/post/<postid>/comment/add')

This API is used to create a comment. The body contains the user id of the member who commented and content.
The user creating the comment must be member of the group.

 For ex : Body
{
"userid":"asdfadsfdsfds54564156",
"content":"my first comment"
}

###(DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')

This Api is used to delete a post. User can delete his post. ADMIN and MODERATOR can delete any post.
The body of the request contains the user id of the member who wants to delete.

 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}

###(DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete') 

This Api is used to delete a comment. User can delete his comment. ADMIN and MODERATOR can delete any comment.
The body of the request contains the user id of the member who wants to delete.

 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}

###(ReadGroupApi, '/api/group/<groupid>/read')

This Api fetches all the posts in a group. You must be a member of the group.
The body of the request contains the user id of the member who wants to access the group. 

 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}

###(GetGroupApi, '/api/group/<groupid>') 

To get a single group information you use this Api. You must be an ADMIN of the group.
The body of the request should contain admin user id.

 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}
                
###(GetPostApi, '/api/group/<groupid>/post/<postid>')   

This Api is used to fetch a particular post. The person accessing must be a member of the group.
 
 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}
         
###(GetCommentApi, '/api/group/<groupid>/comment/<commentid>')

This Api is used to fetch a particular comment. The person accessing must be a member of the group.
 
 For ex : Body
{
"userid":"asdfadsfdsfds54564156"
}
